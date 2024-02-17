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
            help='OpenAPI 3 document path. Supported extensions: .yml, .yaml e .json'
        ),
    ],
    output_path: Annotated[
        str,
        typer.Argument(
            help='Resolved OpenAPI 3 document path to be created. Supported extensions: .yml, .yaml e .json'
        ),
    ],
) -> Literal[True]:
    if not contract_path.endswith(
        ('.yml', '.yaml', '.json')
    ) or not output_path.endswith(('.yml', '.yaml', '.json')):
        raise typer.BadParameter(
            'Only the following extensions are supported: .yml, .yaml e .json'
        )
    resolve(contract_path, output_path)
