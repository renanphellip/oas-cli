import sys
from pathlib import Path
from typing import Any, Dict

from rich import print

from oas_cli.file import read_file


def resolve_external_references(data: object, base_path: str) -> Any:
    if isinstance(data, dict):
        for key, value in data.items():
            if (
                key == '$ref'
                and isinstance(value, str)
                and not value.startswith('#')
            ):
                file_path = f'{base_path}/{value}'
                file_content = read_file(file_path)
                data = resolve_external_references(file_content, base_path)
            else:
                data[key] = resolve_external_references(value, base_path)
    elif isinstance(data, list):
        for i, element in enumerate(data):
            data[i] = resolve_external_references(element, base_path)
    return data


def resolve(contract_path: str) -> Dict[str, Any]:
    try:
        contract_data = read_file(contract_path)

        contract_base_path = Path(contract_path).parent

        resolved_contract_data = resolve_external_references(
            contract_data, contract_base_path
        )
        return resolved_contract_data

    except Exception as error:
        print(f'[red]Failed to resolve the contract: {error}[/red]')
        sys.exit(1)
