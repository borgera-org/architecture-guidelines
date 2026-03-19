from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from pathlib import PureWindowsPath

import yaml
from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "schemas" / "example-manifest.schema.json"
PLACEHOLDER_PATTERN = re.compile(r"\{\{\s*[^}]+\s*\}\}")


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML object at the root.")
    return data


def load_json(path: Path) -> dict:
    import json

    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object at the root.")
    return data


def find_manifests(paths: list[str]) -> list[Path]:
    if paths:
        manifests = [Path(item).resolve() for item in paths]
    else:
        manifests = sorted(REPO_ROOT.glob("examples/**/manifest.yaml"))
    return manifests


def validate_schema(manifest: dict, manifest_path: Path, schema: dict) -> list[str]:
    validator = Draft202012Validator(schema)
    errors = []
    for error in sorted(validator.iter_errors(manifest), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.path) or "<root>"
        errors.append(f"{manifest_path}: schema error at {location}: {error.message}")
    return errors


def validate_snapshot(manifest: dict, manifest_path: Path) -> list[str]:
    errors = []
    scenario_dir = manifest_path.parent

    snapshot_root = scenario_dir / manifest["snapshotRoot"]
    if not snapshot_root.exists():
        errors.append(f"{manifest_path}: snapshot root not found: {manifest['snapshotRoot']}")

    for relative_path in manifest.get("expectedFiles", []):
        expected_path = scenario_dir / relative_path
        if not expected_path.is_file():
            errors.append(f"{manifest_path}: expected file not found: {relative_path}")

    for step in manifest.get("postProcessing", []):
        solution = step.get("solution")
        if solution:
            solution_path = scenario_dir / solution
            if not solution_path.is_file():
                errors.append(f"{manifest_path}: post-processing solution not found: {solution}")

        project = step.get("project")
        if project:
            project_path = scenario_dir / project
            if not project_path.is_file():
                errors.append(f"{manifest_path}: post-processing project not found: {project}")

    if snapshot_root.exists():
        errors.extend(validate_snapshot_paths(snapshot_root, manifest_path))
        errors.extend(validate_snapshot_content(snapshot_root, manifest_path))
        errors.extend(validate_templates_against_snapshot(manifest, manifest_path, scenario_dir, snapshot_root))
        errors.extend(validate_post_processing_content(manifest, manifest_path, scenario_dir))

    return errors


def validate_templates_against_snapshot(
    manifest: dict, manifest_path: Path, scenario_dir: Path, snapshot_root: Path
) -> list[str]:
    errors = []
    excluded_targets = collect_post_processed_targets(manifest, scenario_dir)
    context = manifest["inputs"]

    for template in manifest.get("appliedTemplates", []):
        template_id = template["id"]
        template_root = REPO_ROOT / "templates" / template_id / "files"

        if not template_root.is_dir():
            errors.append(f"{manifest_path}: template payload not found for applied template: {template_id}")
            continue

        for source_path in template_root.rglob("*"):
            if not source_path.is_file():
                continue

            try:
                relative_output = render_output_relative_path(source_path.relative_to(template_root), context)
            except KeyError as exc:
                errors.append(
                    f"{manifest_path}: missing input {exc} while rendering path for template {template_id}: {source_path}"
                )
                continue

            destination_path = snapshot_root / relative_output
            destination_resolved = destination_path.resolve()

            if not destination_path.is_file():
                errors.append(
                    f"{manifest_path}: rendered template file missing from snapshot: {snapshot_root.name}/{relative_output.as_posix()}"
                )
                continue

            if destination_resolved in excluded_targets:
                continue

            if source_path.suffix == ".tpl":
                try:
                    rendered_content = render_text(source_path.read_text(encoding="utf-8"), context)
                except KeyError as exc:
                    errors.append(
                        f"{manifest_path}: missing input {exc} while rendering content for template {template_id}: {source_path}"
                    )
                    continue

                destination_content = destination_path.read_text(encoding="utf-8")
                if destination_content != rendered_content:
                    errors.append(
                        f"{manifest_path}: snapshot content differs from rendered template for {snapshot_root.name}/{relative_output.as_posix()}"
                    )
            else:
                if destination_path.read_bytes() != source_path.read_bytes():
                    errors.append(
                        f"{manifest_path}: snapshot content differs from static template for {snapshot_root.name}/{relative_output.as_posix()}"
                    )

    return errors


def validate_snapshot_paths(snapshot_root: Path, manifest_path: Path) -> list[str]:
    errors = []
    for path in snapshot_root.rglob("*"):
        relative_path = path.relative_to(snapshot_root).as_posix()
        if PLACEHOLDER_PATTERN.search(relative_path):
            errors.append(
                f"{manifest_path}: unresolved placeholder in snapshot path: {snapshot_root.name}/{relative_path}"
            )
    return errors


def validate_snapshot_content(snapshot_root: Path, manifest_path: Path) -> list[str]:
    errors = []
    for path in snapshot_root.rglob("*"):
        if not path.is_file():
            continue

        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        if PLACEHOLDER_PATTERN.search(content):
            relative_path = path.relative_to(snapshot_root).as_posix()
            errors.append(
                f"{manifest_path}: unresolved placeholder in file content: {snapshot_root.name}/{relative_path}"
            )

    return errors


def validate_post_processing_content(manifest: dict, manifest_path: Path, scenario_dir: Path) -> list[str]:
    errors = []
    for step in manifest.get("postProcessing", []):
        if step.get("type") != "solution-add-project":
            continue

        solution_path = scenario_dir / step["solution"]
        project_path = scenario_dir / step["project"]

        if not solution_path.is_file() or not project_path.is_file():
            continue

        solution_text = solution_path.read_text(encoding="utf-8")
        expected_reference = build_solution_project_reference(solution_path, project_path)

        if expected_reference.lower() not in solution_text.lower():
            errors.append(
                f"{manifest_path}: solution {step['solution']} does not reference expected project path {expected_reference}"
            )

    return errors


def build_solution_project_reference(solution_path: Path, project_path: Path) -> str:
    relative_path = os.path.relpath(project_path, solution_path.parent)
    return str(PureWindowsPath(relative_path))


def collect_post_processed_targets(manifest: dict, scenario_dir: Path) -> set[Path]:
    targets: set[Path] = set()
    for step in manifest.get("postProcessing", []):
        if step.get("type") == "solution-add-project" and "solution" in step:
            targets.add((scenario_dir / step["solution"]).resolve())
    return targets


def render_output_relative_path(source_relative_path: Path, context: dict) -> Path:
    rendered_parts = []
    for index, part in enumerate(source_relative_path.parts):
        rendered_part = render_text(part, context)
        if index == len(source_relative_path.parts) - 1 and rendered_part.endswith(".tpl"):
            rendered_part = rendered_part[:-4]
        rendered_parts.append(rendered_part)
    return Path(*rendered_parts)


def render_text(template_text: str, context: dict) -> str:
    def replace(match: re.Match[str]) -> str:
        key = match.group(0)[2:-2].strip()
        if key not in context:
            raise KeyError(key)
        return stringify_value(context[key])

    return PLACEHOLDER_PATTERN.sub(replace, template_text)


def stringify_value(value: object) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def validate_manifest(manifest_path: Path, schema: dict) -> list[str]:
    if not manifest_path.is_file():
        return [f"{manifest_path}: manifest file not found."]

    try:
        manifest = load_yaml(manifest_path)
    except Exception as exc:  # noqa: BLE001
        return [f"{manifest_path}: failed to parse YAML: {exc}"]

    errors = []
    errors.extend(validate_schema(manifest, manifest_path, schema))

    if not errors:
        errors.extend(validate_snapshot(manifest, manifest_path))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate example manifests against the platform schema and snapshot files."
    )
    parser.add_argument(
        "manifests",
        nargs="*",
        help="Optional manifest paths. If omitted, validates every examples/**/manifest.yaml file.",
    )
    args = parser.parse_args()

    manifests = find_manifests(args.manifests)
    if not manifests:
        print("No manifest.yaml files found.")
        return 1

    try:
        schema = load_json(SCHEMA_PATH)
    except Exception as exc:  # noqa: BLE001
        print(f"Failed to load schema {SCHEMA_PATH}: {exc}")
        return 1

    failures = []
    for manifest_path in manifests:
        errors = validate_manifest(manifest_path, schema)
        if errors:
            failures.extend(errors)
        else:
            print(f"OK: {manifest_path}")

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
