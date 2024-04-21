from typing import Literal

import typer
from rich import print
from typing_extensions import Annotated

from oas_cli.file import (
    validate_file_extension,
    validate_file_path,
    write_file
)
from oas_cli.resolver import Resolver


def resolve(
    contract_path: Annotated[
        str,
        typer.Argument(
            help='OpenAPI 3 document path. Supported extensions: .yml, .yaml, .json'
        ),
    ],
    output_path: Annotated[
        str,
        typer.Argument(
            help='Resolved OpenAPI 3 document path to be created. Supported extensions: .yml, .yaml, .json'
        ),
    ],
) -> Literal[True]:
    supported_extensions = ('.yml', '.yaml', '.json')
    validate_file_path(contract_path, supported_extensions)
    validate_file_extension(output_path, supported_extensions)
    resolver = Resolver()
    resolved_contract = resolver.resolve(contract_path)
    absolute_output_path = write_file(output_path, resolved_contract)
    print(
        f'[green]Success to resolve the contract: {absolute_output_path}[/green]'
    )
