from typing import Literal

import typer
from typing_extensions import Annotated

from oas_cli.resolve import resolve

cli = typer.Typer(help='OpenAPI Specification CLI', no_args_is_help=True)


@cli.command('resolve')
def resolve_input(
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
    supported_file_extensions = ('.yml', '.yaml', '.json')
    if not contract_path.endswith(
        supported_file_extensions
    ) or not output_path.endswith(supported_file_extensions):
        raise typer.BadParameter(
            f'Only the following extensions are supported: {supported_file_extensions}'
        )
    resolve(contract_path, output_path)
