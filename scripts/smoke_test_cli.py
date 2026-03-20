from __future__ import annotations

import argparse
import shutil
import sys
import uuid
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from cli.app import scaffold_repository
from scripts import validate_example


def find_manifests(paths: list[str]) -> list[Path]:
    if paths:
        return [Path(item).resolve() for item in paths]
    return sorted(REPO_ROOT.glob("examples/**/manifest.yaml"))


def smoke_test_manifest(manifest_path: Path, schema: dict) -> list[str]:
    manifest = validate_example.load_yaml(manifest_path)
    manifest_errors = validate_example.validate_schema(manifest, manifest_path, schema)
    if manifest_errors:
        return manifest_errors

    temp_root_parent = REPO_ROOT / ".tmp-cli-smoke"
    temp_root_parent.mkdir(parents=True, exist_ok=True)
    temp_root = temp_root_parent / f"run-{uuid.uuid4().hex}"
    temp_root.mkdir(parents=True, exist_ok=False)

    try:
        scaffold_repository(
            archetype_id=manifest["archetypeId"],
            destination_parent=temp_root,
            provided_values=manifest["inputs"],
        )
        temp_manifest_path = temp_root / "manifest.yaml"
        return validate_example.validate_snapshot(manifest, temp_manifest_path)
    finally:
        shutil.rmtree(temp_root, ignore_errors=True)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scaffold official example scenarios with the reference CLI and validate the generated result."
    )
    parser.add_argument(
        "manifests",
        nargs="*",
        help="Optional manifest paths. If omitted, smoke-tests every examples/**/manifest.yaml file.",
    )
    args = parser.parse_args()

    manifests = find_manifests(args.manifests)
    if not manifests:
        print("No manifest.yaml files found.")
        return 1

    try:
        schema = validate_example.load_json(validate_example.SCHEMA_PATH)
    except Exception as exc:  # noqa: BLE001
        print(f"Failed to load schema {validate_example.SCHEMA_PATH}: {exc}")
        return 1

    failures: list[str] = []
    for manifest_path in manifests:
        errors = smoke_test_manifest(manifest_path, schema)
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
