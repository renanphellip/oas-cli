from typing import Optional

import typer
from typing_extensions import Annotated

from oas_cli.entities.custom import OutputFormat
from oas_cli.file import (
    validate_file_extension,
    validate_file_path,
    write_file
)
from oas_cli.logger import print_error_messages
from oas_cli.validate import Validator


def validate(
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
    validator = Validator()
    custom_functions_path = 'oas_cli/custom_functions'
    error_message_collection = validator.validate(
        contract_path, ruleset_path, custom_functions_path
    )
    if results_path:
        write_file(results_path, error_message_collection)
    if output_format != OutputFormat.NONE:
        print_error_messages(output_format, error_message_collection)
    return True
