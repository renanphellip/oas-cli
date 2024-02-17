import sys
from pathlib import Path
from typing import Literal

from rich import print

from oas_cli.file import read_file, write_file


def resolve_external_references(data: object, base_path: str):
    if isinstance(data, dict):
        for key, value in data.items():
            # Se a referência não começar com '#', é uma referência externa
            if (
                key == '$ref'
                and isinstance(value, str)
                and not value.startswith('#')
            ):
                file_path = f'{base_path}/{value}'  # Caminho absoluto do arquivo referenciado
                file_content = read_file(file_path)
                data = resolve_external_references(file_content, base_path)
            else:
                data[key] = resolve_external_references(value, base_path)
    elif isinstance(data, list):
        for i, element in enumerate(data):
            data[i] = resolve_external_references(element, base_path)
    return data


def resolve(contract_path: str, output_path: str) -> Literal[True]:
    try:
        contract_data = read_file(contract_path)

        # Obtendo o diretório base para referências externas
        contract_base_path = Path(contract_path).parent

        # Resolvendo todas referências externas
        resolved_contract_data = resolve_external_references(
            contract_data, contract_base_path
        )

        # Salvando o contrato resolvido
        absolute_output_path = write_file(output_path, resolved_contract_data)
        print(
            f'[green]Success to resolve the contract: {absolute_output_path}[/green]'
        )
        return True

    except Exception as error:
        print(f'[red]Failed to resolve the contract: {error}[/red]')
        sys.exit(1)
