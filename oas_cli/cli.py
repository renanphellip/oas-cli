from typing import Literal, Optional

import typer
from rich import print
from typing_extensions import Annotated

from oas_cli.entities import OutputFormat
from oas_cli.file import (validate_file_extension, validate_file_path,
                          write_file)
from oas_cli.logger import print_error_messages
from oas_cli.resolve import resolve
from oas_cli.validate import validate

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
    supported_extensions = ('.yml', '.yaml', '.json')
    validate_file_path(contract_path, supported_extensions)
    validate_file_extension(output_path, supported_extensions)
    resolved_contract = resolve(contract_path)
    absolute_output_path = write_file(output_path, resolved_contract)
    print(
        f'[green]Success to resolve the contract: {absolute_output_path}[/green]'
    )


@cli.command('validate')
def validate_input(
    contract_path: Annotated[
        str,
        typer.Argument(
            help='OpenAPI 3 document path. Supported extensions: .yml, .yaml, .json'
        ),
    ],
    ruleset_path: Annotated[
        str,
        typer.Argument(help='Ruleset path. Supported extensions: .yml, .yaml'),
    ],
    results_path: Annotated[
        Optional[str],
        typer.Argument(
            help='Validation results file path to be created. Supported extension: .json, .txt'
        ),
    ] = None,
    resolve_contract: Annotated[
        bool,
        typer.Option(
            help='Resolve external references from contract before validate.'
        ),
    ] = False,
    output_format: Annotated[
        OutputFormat,
        typer.Option(
            help='Output format of results in the console. This option does not affect the results_path argument.',
            case_sensitive=False,
        ),
    ] = OutputFormat.TXT,
):
    contract_supported_extensions = ('.yml', '.yaml', '.json')
    validate_file_path(contract_path, contract_supported_extensions)
    ruleset_supported_extensions = ('.yml', '.yaml')
    validate_file_path(ruleset_path, ruleset_supported_extensions)
    if results_path:
        results_supported_extensions = ('.json', '.txt')
        validate_file_extension(results_path, results_supported_extensions)
    error_message_collection = validate(
        contract_path, ruleset_path, resolve_contract
    )
    if results_path:
        write_file(results_path, error_message_collection)
    if output_format != OutputFormat.NONE:
        print_error_messages(output_format, error_message_collection)
