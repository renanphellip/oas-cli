import sys
from pathlib import Path
from typing import Any, Dict

from rich.console import Console
from rich.markup import escape

from oas_cli.file import read_file


class Resolver:
    def __init__(self):
        self.__console = Console(highlight=False)

    def __resolve_external_references(self, data: object, base_path: str) -> Any:
        if isinstance(data, dict):
            for key, value in data.items():
                if (
                    key == '$ref'
                    and isinstance(value, str)
                    and not value.startswith('#')
                ):
                    file_path = f'{base_path}/{value}'
                    file_content = read_file(file_path)
                    data = self.__resolve_external_references(file_content, base_path)
                else:
                    data[key] = self.__resolve_external_references(value, base_path)
        elif isinstance(data, list):
            for i, element in enumerate(data):
                data[i] = self.__resolve_external_references(element, base_path)
        return data


    def resolve(self, contract_path: str) -> Dict[str, Any]:
        try:
            contract_data = read_file(contract_path)

            contract_base_path = Path(contract_path).parent

            resolved_contract_data = self.__resolve_external_references(
                contract_data, contract_base_path
            )
            return resolved_contract_data

        except Exception as error:
            self.__console.print(f'[red]Failed to resolve the contract: {escape(str(error))}[/red]')
            sys.exit(1)
