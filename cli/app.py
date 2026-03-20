from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import uuid
from dataclasses import dataclass
from pathlib import Path, PureWindowsPath
from typing import Any

import yaml
from jsonschema import Draft202012Validator


CSHARP_PROJECT_TYPE_GUID = "9A19103F-16F7-4668-BE54-9A1E7A4F7556"
CONTRACTS_ROOT_ENV_VAR = "AG_CONTRACTS_ROOT"
BOOLEAN_TRUE = {"true", "1", "yes", "y"}
BOOLEAN_FALSE = {"false", "0", "no", "n"}
KEBAB_CASE_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PASCAL_SEGMENT_PATTERN = re.compile(r"^[A-Z][A-Za-z0-9]*$")
PLACEHOLDER_PATTERN = re.compile(r"\{\{\s*[^}]+\s*\}\}")
WHEN_PATTERN = re.compile(r"^\s*([a-z][A-Za-z0-9]*)\s*==\s*(true|false)\s*$")


class CliError(Exception):
    pass


@dataclass(frozen=True)
class ContractsRepository:
    root: Path
    archetypes_root: Path
    templates_root: Path
    archetype_schema_path: Path
    post_processing_schema_path: Path

    @classmethod
    def from_root(cls, root: Path) -> "ContractsRepository":
        resolved_root = root.expanduser().resolve()
        return cls(
            root=resolved_root,
            archetypes_root=resolved_root / "archetypes",
            templates_root=resolved_root / "templates",
            archetype_schema_path=resolved_root / "schemas" / "archetype.schema.json",
            post_processing_schema_path=resolved_root / "schemas" / "post-processing.schema.json",
        )


@dataclass
class ScaffoldResult:
    archetype_id: str
    repository_path: Path
    applied_templates: list[str]
    executed_post_processing: list[str]


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        contracts = resolve_contracts_repository(args.contracts_root)

        if args.command == "list-archetypes":
            return run_list_archetypes(contracts)

        if args.command == "scaffold":
            provided_values: dict[str, Any] = {}
            if args.values_file:
                provided_values.update(load_values_file(Path(args.values_file)))
            provided_values.update(parse_set_arguments(args.set_values))

            result = scaffold_repository(
                archetype_id=args.archetype_id,
                destination_parent=Path(args.destination),
                provided_values=provided_values,
                contracts=contracts,
            )
            print(f"Scaffolded {result.archetype_id} into {result.repository_path}")
            print(f"Applied templates: {', '.join(result.applied_templates)}")
            if result.executed_post_processing:
                print(f"Post-processing: {', '.join(result.executed_post_processing)}")
            else:
                print("Post-processing: none")
            return 0

        parser.print_help()
        return 1
    except CliError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Reference CLI for scaffolding repositories from the platform contracts."
    )
    add_contracts_root_argument(parser)
    subparsers = parser.add_subparsers(dest="command")

    list_parser = subparsers.add_parser("list-archetypes", help="List archetypes published in the contracts root.")
    add_contracts_root_argument(list_parser)

    scaffold_parser = subparsers.add_parser(
        "scaffold",
        help="Materialize a repository from an archetype definition.",
    )
    add_contracts_root_argument(scaffold_parser)
    scaffold_parser.add_argument("archetype_id", help="Archetype identifier, for example api-dotnet.")
    scaffold_parser.add_argument(
        "--destination",
        default=".",
        help="Parent directory where the repository folder will be created. Defaults to the current directory.",
    )
    scaffold_parser.add_argument(
        "--values-file",
        help="Optional YAML file containing input values keyed by archetype input id.",
    )
    scaffold_parser.add_argument(
        "--set",
        dest="set_values",
        action="append",
        default=[],
        help="Override or provide an input value using KEY=VALUE. Can be repeated.",
    )

    return parser


def add_contracts_root_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--contracts-root",
        help=(
            "Path to the architecture-guidelines contracts repository. "
            f"Defaults to ${CONTRACTS_ROOT_ENV_VAR} or an inferred source checkout when available."
        ),
    )


def run_list_archetypes(contracts: ContractsRepository) -> int:
    for definition_path in sorted(contracts.archetypes_root.glob("*/definition.yaml")):
        definition = load_yaml(definition_path)
        print(f"{definition['id']}\t{definition['status']}\t{definition['name']}")
    return 0


def load_values_file(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise CliError(f"Values file not found: {path}")

    values = load_yaml(path)
    if not isinstance(values, dict):
        raise CliError(f"Values file must contain a YAML object: {path}")

    return values


def parse_set_arguments(raw_values: list[str]) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for raw_value in raw_values:
        if "=" not in raw_value:
            raise CliError(f"Invalid --set argument {raw_value!r}. Expected KEY=VALUE.")
        key, value = raw_value.split("=", 1)
        key = key.strip()
        if not key:
            raise CliError(f"Invalid --set argument {raw_value!r}. Key cannot be empty.")
        parsed[key] = value
    return parsed


def scaffold_repository(
    archetype_id: str,
    destination_parent: Path,
    provided_values: dict[str, Any],
    contracts: ContractsRepository | None = None,
    contracts_root: str | Path | None = None,
) -> ScaffoldResult:
    active_contracts = contracts or resolve_contracts_repository(contracts_root)
    definition_path = active_contracts.archetypes_root / archetype_id / "definition.yaml"
    archetype_schema = load_json(active_contracts.archetype_schema_path)
    post_processing_schema = load_json(active_contracts.post_processing_schema_path)

    errors = validate_definition(definition_path, archetype_schema, post_processing_schema, active_contracts)
    if errors:
        raise CliError("\n".join(errors))

    definition = load_yaml(definition_path)
    resolved_values = resolve_inputs(definition, provided_values)
    validate_constraints(definition, resolved_values)

    destination_parent = destination_parent.resolve()
    destination_parent.mkdir(parents=True, exist_ok=True)

    repository_path = destination_parent / stringify_value(resolved_values["repositoryName"])
    ensure_destination_is_writable(repository_path)

    applied_templates: list[str] = []
    for template_id in select_templates(definition, resolved_values):
        apply_template(template_id, repository_path, resolved_values, active_contracts)
        applied_templates.append(template_id)

    executed_post_processing = execute_post_processing(definition, repository_path, resolved_values)

    return ScaffoldResult(
        archetype_id=archetype_id,
        repository_path=repository_path,
        applied_templates=applied_templates,
        executed_post_processing=executed_post_processing,
    )


def resolve_contracts_repository(requested_root: str | Path | None) -> ContractsRepository:
    if requested_root:
        return build_contracts_repository(Path(requested_root), "--contracts-root")

    environment_root = os.getenv(CONTRACTS_ROOT_ENV_VAR)
    if environment_root:
        return build_contracts_repository(Path(environment_root), CONTRACTS_ROOT_ENV_VAR)

    inferred_root = infer_source_contracts_root()
    if inferred_root is not None:
        return build_contracts_repository(inferred_root, "inferred source checkout")

    current_working_directory = Path.cwd().resolve()
    if looks_like_contracts_root(current_working_directory):
        return build_contracts_repository(current_working_directory, "current working directory")

    raise CliError(
        "Contracts root could not be inferred. Use --contracts-root or set "
        f"{CONTRACTS_ROOT_ENV_VAR} to the architecture-guidelines repository clone."
    )


def infer_source_contracts_root() -> Path | None:
    source_root = Path(__file__).resolve().parent.parent
    if looks_like_contracts_root(source_root):
        return source_root
    return None


def build_contracts_repository(root: Path, source_label: str) -> ContractsRepository:
    contracts = ContractsRepository.from_root(root)
    missing = missing_contract_artifacts(contracts)
    if missing:
        formatted_missing = ", ".join(missing)
        raise CliError(
            f"{source_label} does not point to a valid contracts repository: {contracts.root}. "
            f"Missing: {formatted_missing}"
        )
    return contracts


def looks_like_contracts_root(root: Path) -> bool:
    contracts = ContractsRepository.from_root(root)
    return not missing_contract_artifacts(contracts)


def missing_contract_artifacts(contracts: ContractsRepository) -> list[str]:
    missing: list[str] = []
    if not contracts.archetypes_root.is_dir():
        missing.append("archetypes/")
    if not contracts.templates_root.is_dir():
        missing.append("templates/")
    if not contracts.archetype_schema_path.is_file():
        missing.append("schemas/archetype.schema.json")
    if not contracts.post_processing_schema_path.is_file():
        missing.append("schemas/post-processing.schema.json")
    return missing


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML object at the root.")
    return data


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object at the root.")
    return data


def validate_definition(
    definition_path: Path,
    archetype_schema: dict[str, Any],
    post_processing_schema: dict[str, Any],
    contracts: ContractsRepository,
) -> list[str]:
    if not definition_path.is_file():
        return [f"{definition_path}: definition file not found."]

    try:
        definition = load_yaml(definition_path)
    except Exception as exc:  # noqa: BLE001
        return [f"{definition_path}: failed to parse YAML: {exc}"]

    errors: list[str] = []
    errors.extend(validate_schema(definition, definition_path, archetype_schema))

    if not errors:
        errors.extend(validate_archetype_structure(definition, definition_path, contracts))
        errors.extend(validate_when_semantics(definition, definition_path))
        errors.extend(validate_post_processing(definition, definition_path, post_processing_schema))

    return errors


def validate_schema(definition: dict[str, Any], definition_path: Path, schema: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema)
    errors: list[str] = []
    for error in sorted(validator.iter_errors(definition), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.path) or "<root>"
        errors.append(f"{definition_path}: schema error at {location}: {error.message}")
    return errors


def validate_archetype_structure(
    definition: dict[str, Any],
    definition_path: Path,
    contracts: ContractsRepository,
) -> list[str]:
    errors: list[str] = []
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
        template_root = contracts.templates_root / template_id
        if not template_root.is_dir():
            errors.append(f"{definition_path}: referenced template not found: {template_id}")

    return errors


def validate_when_semantics(definition: dict[str, Any], definition_path: Path) -> list[str]:
    errors: list[str] = []
    boolean_inputs = {
        item.get("id")
        for item in definition.get("inputs", [])
        if isinstance(item, dict) and item.get("type") == "boolean" and isinstance(item.get("id"), str)
    }

    for index, entry in enumerate(definition.get("templateSet", {}).get("templates", [])):
        if isinstance(entry, dict) and isinstance(entry.get("when"), str):
            errors.extend(
                validate_when_expression(
                    entry["when"],
                    definition_path,
                    f"templateSet.templates[{index}].when",
                    boolean_inputs,
                )
            )

    for index, step in enumerate(definition.get("postProcessing", [])):
        if isinstance(step, dict) and isinstance(step.get("when"), str):
            errors.extend(
                validate_when_expression(
                    step["when"],
                    definition_path,
                    f"postProcessing[{index}].when",
                    boolean_inputs,
                )
            )

    return errors


def validate_when_expression(
    expression: str,
    definition_path: Path,
    location: str,
    boolean_inputs: set[str],
) -> list[str]:
    match = WHEN_PATTERN.fullmatch(expression)
    if not match:
        return [
            (
                f"{definition_path}: {location} uses unsupported when expression {expression!r}. "
                "Supported format is '<booleanInput> == true|false'."
            )
        ]

    input_id = match.group(1)
    if input_id not in boolean_inputs:
        return [
            (
                f"{definition_path}: {location} references {input_id!r}, "
                "but only declared boolean inputs may be used in when expressions."
            )
        ]

    return []


def validate_post_processing(
    definition: dict[str, Any],
    definition_path: Path,
    schema: dict[str, Any],
) -> list[str]:
    validator = Draft202012Validator(schema)
    errors: list[str] = []
    for index, step in enumerate(definition.get("postProcessing", [])):
        for error in sorted(validator.iter_errors(step), key=lambda item: list(item.path)):
            location = ".".join(str(part) for part in error.path) or "<root>"
            errors.append(f"{definition_path}: postProcessing[{index}] error at {location}: {error.message}")
    return errors


def find_duplicates(values: list[str]) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates


def resolve_inputs(definition: dict[str, Any], provided_values: dict[str, Any]) -> dict[str, Any]:
    input_definitions = definition.get("inputs", [])
    known_inputs = {item["id"]: item for item in input_definitions}

    unknown_inputs = sorted(set(provided_values) - set(known_inputs))
    if unknown_inputs:
        raise CliError(f"Unknown inputs for archetype {definition['id']}: {', '.join(unknown_inputs)}")

    resolved: dict[str, Any] = {}
    for input_definition in input_definitions:
        input_id = input_definition["id"]
        has_default = "default" in input_definition

        if has_default:
            resolved[input_id] = input_definition["default"]

        if input_id in provided_values:
            resolved[input_id] = coerce_value(provided_values[input_id], input_definition["type"], input_id)

        if input_definition.get("required") and input_id not in resolved:
            raise CliError(f"Missing required input: {input_id}")

    return resolved


def coerce_value(raw_value: Any, expected_type: str, input_id: str) -> Any:
    if expected_type == "string":
        if isinstance(raw_value, (dict, list)):
            raise CliError(f"Input {input_id} must be a string.")
        return str(raw_value)

    if expected_type == "boolean":
        if isinstance(raw_value, bool):
            return raw_value
        if isinstance(raw_value, str):
            normalized = raw_value.strip().lower()
            if normalized in BOOLEAN_TRUE:
                return True
            if normalized in BOOLEAN_FALSE:
                return False
        raise CliError(f"Input {input_id} must be a boolean value.")

    if expected_type == "integer":
        if isinstance(raw_value, bool):
            raise CliError(f"Input {input_id} must be an integer.")
        if isinstance(raw_value, int):
            return raw_value
        if isinstance(raw_value, str):
            try:
                return int(raw_value.strip())
            except ValueError as exc:
                raise CliError(f"Input {input_id} must be an integer.") from exc
        raise CliError(f"Input {input_id} must be an integer.")

    if expected_type == "number":
        if isinstance(raw_value, bool):
            raise CliError(f"Input {input_id} must be a number.")
        if isinstance(raw_value, (int, float)):
            return raw_value
        if isinstance(raw_value, str):
            try:
                return float(raw_value.strip())
            except ValueError as exc:
                raise CliError(f"Input {input_id} must be a number.") from exc
        raise CliError(f"Input {input_id} must be a number.")

    raise CliError(f"Unsupported input type {expected_type!r} for {input_id}")


def validate_constraints(definition: dict[str, Any], resolved_values: dict[str, Any]) -> None:
    for constraint in definition.get("constraints", []):
        constraint_id = constraint["id"]

        if constraint_id == "repository-name-kebab-case":
            repository_name = resolved_values.get("repositoryName")
            if not isinstance(repository_name, str) or not KEBAB_CASE_PATTERN.fullmatch(repository_name):
                raise CliError("Constraint repository-name-kebab-case violated by repositoryName.")

        if constraint_id == "root-namespace-pascal-case":
            root_namespace = resolved_values.get("rootNamespace")
            if not isinstance(root_namespace, str):
                raise CliError("Constraint root-namespace-pascal-case violated by rootNamespace.")
            segments = root_namespace.split(".")
            if any(not PASCAL_SEGMENT_PATTERN.fullmatch(segment) for segment in segments):
                raise CliError("Constraint root-namespace-pascal-case violated by rootNamespace.")


def ensure_destination_is_writable(repository_path: Path) -> None:
    if repository_path.exists():
        if not repository_path.is_dir():
            raise CliError(f"Destination path already exists and is not a directory: {repository_path}")
        if any(repository_path.iterdir()):
            raise CliError(f"Destination repository path already exists and is not empty: {repository_path}")
    else:
        repository_path.mkdir(parents=True, exist_ok=False)


def select_templates(definition: dict[str, Any], resolved_values: dict[str, Any]) -> list[str]:
    selected: list[str] = []
    for entry in definition["templateSet"]["templates"]:
        if isinstance(entry, str):
            selected.append(entry)
            continue

        if evaluate_when(entry.get("when"), resolved_values):
            selected.append(entry["id"])

    return selected


def evaluate_when(expression: str | None, context: dict[str, Any]) -> bool:
    if not expression:
        return True

    match = WHEN_PATTERN.fullmatch(expression)
    if not match:
        raise CliError(f"Unsupported when expression: {expression}")

    input_id = match.group(1)
    expected_value = match.group(2) == "true"
    actual_value = context.get(input_id)

    if not isinstance(actual_value, bool):
        raise CliError(f"When expression references non-boolean input: {input_id}")

    return actual_value is expected_value


def apply_template(
    template_id: str,
    repository_path: Path,
    context: dict[str, Any],
    contracts: ContractsRepository,
) -> None:
    template_root = contracts.templates_root / template_id / "files"
    if not template_root.is_dir():
        raise CliError(f"Template payload not found: {template_id}")

    for source_path in sorted(template_root.rglob("*")):
        if not source_path.is_file():
            continue

        try:
            relative_output_path = render_output_relative_path(source_path.relative_to(template_root), context)
        except KeyError as exc:
            raise CliError(f"Missing value for placeholder {exc.args[0]!r}.") from exc

        destination_path = repository_path / relative_output_path
        destination_path.parent.mkdir(parents=True, exist_ok=True)

        if destination_path.exists():
            raise CliError(f"Template conflict while writing {destination_path}")

        if source_path.suffix == ".tpl":
            rendered_content = render_template(source_path.read_text(encoding="utf-8"), context)
            write_text_file(destination_path, rendered_content)
        else:
            shutil.copyfile(source_path, destination_path)


def render_output_relative_path(source_relative_path: Path, context: dict[str, Any]) -> Path:
    rendered_parts = []
    for index, part in enumerate(source_relative_path.parts):
        rendered_part = render_text(part, context)
        if index == len(source_relative_path.parts) - 1 and rendered_part.endswith(".tpl"):
            rendered_part = rendered_part[:-4]
        rendered_parts.append(rendered_part)
    return Path(*rendered_parts)


def render_text(template_text: str, context: dict[str, Any]) -> str:
    def replace(match: re.Match[str]) -> str:
        key = match.group(0)[2:-2].strip()
        if key not in context:
            raise KeyError(key)
        return stringify_value(context[key])

    return PLACEHOLDER_PATTERN.sub(replace, template_text)


def write_text_file(path: Path, content: str) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(content)


def execute_post_processing(definition: dict[str, Any], repository_path: Path, context: dict[str, Any]) -> list[str]:
    executed: list[str] = []
    for step in definition.get("postProcessing", []):
        if not evaluate_when(step.get("when"), context):
            continue

        step_type = step["type"]
        if step_type != "solution-add-project":
            raise CliError(f"Unsupported post-processing step: {step_type}")

        solution_path = repository_path / render_template(step["solution"], context)
        project_path = repository_path / render_template(step["project"], context)
        add_project_to_solution(solution_path, project_path)
        executed.append(f"{step_type}:{project_path.relative_to(repository_path).as_posix()}")

    return executed


def add_project_to_solution(solution_path: Path, project_path: Path) -> None:
    if not solution_path.is_file():
        raise CliError(f"Solution not found for post-processing: {solution_path}")
    if not project_path.is_file():
        raise CliError(f"Project not found for post-processing: {project_path}")

    existing_projects = parse_solution_projects(solution_path)
    project_reference = build_solution_project_reference(solution_path, project_path)
    normalized_reference = project_reference.lower()

    if any(project["path"].lower() == normalized_reference for project in existing_projects):
        return

    existing_projects.append(
        {
            "name": project_path.stem,
            "path": project_reference,
            "guid": deterministic_guid(solution_path, normalized_reference),
        }
    )

    write_solution(solution_path, existing_projects)


def build_solution_project_reference(solution_path: Path, project_path: Path) -> str:
    relative_path = os.path.relpath(project_path, solution_path.parent)
    return str(PureWindowsPath(relative_path))


def parse_solution_projects(solution_path: Path) -> list[dict[str, str]]:
    projects: list[dict[str, str]] = []
    solution_text = solution_path.read_text(encoding="utf-8")

    for line in solution_text.splitlines():
        if not line.startswith('Project("'):
            continue

        parts = line.split('"')
        if len(parts) < 8:
            continue

        projects.append(
            {
                "name": parts[3],
                "path": parts[5],
                "guid": parts[7].strip("{}").upper(),
            }
        )

    return projects


def write_solution(solution_path: Path, projects: list[dict[str, str]]) -> None:
    lines = [
        "Microsoft Visual Studio Solution File, Format Version 12.00",
        "# Visual Studio Version 17",
        "VisualStudioVersion = 17.0.31903.59",
        "MinimumVisualStudioVersion = 10.0.40219.1",
    ]

    for project in projects:
        lines.append(
            f'Project("{{{CSHARP_PROJECT_TYPE_GUID}}}") = "{project["name"]}", "{project["path"]}", "{{{project["guid"]}}}"'
        )
        lines.append("EndProject")

    lines.extend(
        [
            "Global",
            "\tGlobalSection(SolutionConfigurationPlatforms) = preSolution",
            "\t\tDebug|Any CPU = Debug|Any CPU",
            "\t\tRelease|Any CPU = Release|Any CPU",
            "\tEndGlobalSection",
        ]
    )

    if projects:
        lines.append("\tGlobalSection(ProjectConfigurationPlatforms) = postSolution")
        for project in projects:
            lines.append(f'\t\t{{{project["guid"]}}}.Debug|Any CPU.ActiveCfg = Debug|Any CPU')
            lines.append(f'\t\t{{{project["guid"]}}}.Debug|Any CPU.Build.0 = Debug|Any CPU')
            lines.append(f'\t\t{{{project["guid"]}}}.Release|Any CPU.ActiveCfg = Release|Any CPU')
            lines.append(f'\t\t{{{project["guid"]}}}.Release|Any CPU.Build.0 = Release|Any CPU')
        lines.append("\tEndGlobalSection")

    lines.extend(
        [
            "\tGlobalSection(SolutionProperties) = preSolution",
            "\t\tHideSolutionNode = FALSE",
            "\tEndGlobalSection",
            "EndGlobal",
            "",
        ]
    )

    write_text_file(solution_path, "\n".join(lines))


def deterministic_guid(solution_path: Path, project_reference: str) -> str:
    seed = f"{solution_path.name}:{project_reference}"
    return str(uuid.uuid5(uuid.NAMESPACE_URL, seed)).upper()


def stringify_value(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def render_template(template_text: str, context: dict[str, Any]) -> str:
    try:
        return render_text(template_text, context)
    except KeyError as exc:
        raise CliError(f"Missing value for placeholder {exc.args[0]!r}.") from exc
