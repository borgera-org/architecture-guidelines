from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parent.parent
ARCHETYPES_ROOT = REPO_ROOT / "archetypes"
TEMPLATES_ROOT = REPO_ROOT / "templates"
ARCHETYPE_SCHEMA_PATH = REPO_ROOT / "schemas" / "archetype.schema.json"
POST_PROCESSING_SCHEMA_PATH = REPO_ROOT / "schemas" / "post-processing.schema.json"


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML object at the root.")
    return data


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object at the root.")
    return data


def find_definitions(paths: list[str]) -> list[Path]:
    if paths:
        return [Path(item).resolve() for item in paths]
    return sorted(ARCHETYPES_ROOT.glob("*/definition.yaml"))


def validate_schema(definition: dict, definition_path: Path, schema: dict) -> list[str]:
    validator = Draft202012Validator(schema)
    errors = []
    for error in sorted(validator.iter_errors(definition), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.path) or "<root>"
        errors.append(f"{definition_path}: schema error at {location}: {error.message}")
    return errors


def validate_archetype_structure(definition: dict, definition_path: Path) -> list[str]:
    errors = []
    archetype_dir = definition_path.parent
    expected_id = definition.get("id")

    if expected_id and archetype_dir.name != expected_id:
        errors.append(
            f"{definition_path}: archetype directory name {archetype_dir.name!r} must match id {expected_id!r}"
        )

    readme_path = archetype_dir / "README.md"
    if not readme_path.is_file():
        errors.append(f"{definition_path}: README.md not found for archetype {archetype_dir.name}")

    input_ids = [item.get("id") for item in definition.get("inputs", []) if isinstance(item, dict)]
    if len(input_ids) != len(set(input_ids)):
        errors.append(f"{definition_path}: duplicate input ids found in inputs")

    template_ids: list[str] = []
    for entry in definition.get("templateSet", {}).get("templates", []):
        if isinstance(entry, str):
            template_ids.append(entry)
        elif isinstance(entry, dict):
            template_ids.append(entry.get("id", ""))

    duplicates = find_duplicates(template_ids)
    if duplicates:
        duplicate_list = ", ".join(sorted(duplicates))
        errors.append(f"{definition_path}: duplicate template ids found in templateSet: {duplicate_list}")

    for template_id in template_ids:
        template_root = TEMPLATES_ROOT / template_id
        if not template_root.is_dir():
            errors.append(f"{definition_path}: referenced template not found: {template_id}")

    return errors


def validate_post_processing(definition: dict, definition_path: Path, schema: dict) -> list[str]:
    validator = Draft202012Validator(schema)
    errors = []
    for index, step in enumerate(definition.get("postProcessing", [])):
        for error in sorted(validator.iter_errors(step), key=lambda item: list(item.path)):
            location = ".".join(str(part) for part in error.path) or "<root>"
            errors.append(
                f"{definition_path}: postProcessing[{index}] error at {location}: {error.message}"
            )
    return errors


def find_duplicates(values: list[str]) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates


def validate_definition(definition_path: Path, archetype_schema: dict, post_processing_schema: dict) -> list[str]:
    if not definition_path.is_file():
        return [f"{definition_path}: definition file not found."]

    try:
        definition = load_yaml(definition_path)
    except Exception as exc:  # noqa: BLE001
        return [f"{definition_path}: failed to parse YAML: {exc}"]

    errors = []
    errors.extend(validate_schema(definition, definition_path, archetype_schema))

    if not errors:
        errors.extend(validate_archetype_structure(definition, definition_path))
        errors.extend(validate_post_processing(definition, definition_path, post_processing_schema))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate archetype definitions against platform schemas and local repository structure."
    )
    parser.add_argument(
        "definitions",
        nargs="*",
        help="Optional definition.yaml paths. If omitted, validates every archetypes/*/definition.yaml file.",
    )
    args = parser.parse_args()

    definitions = find_definitions(args.definitions)
    if not definitions:
        print("No definition.yaml files found.")
        return 1

    try:
        archetype_schema = load_json(ARCHETYPE_SCHEMA_PATH)
        post_processing_schema = load_json(POST_PROCESSING_SCHEMA_PATH)
    except Exception as exc:  # noqa: BLE001
        print(f"Failed to load schemas: {exc}")
        return 1

    failures = []
    for definition_path in definitions:
        errors = validate_definition(definition_path, archetype_schema, post_processing_schema)
        if errors:
            failures.extend(errors)
        else:
            print(f"OK: {definition_path}")

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
