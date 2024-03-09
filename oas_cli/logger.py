import json
from typing import Literal

from rich import print

from oas_cli.entities import ErrorMessageCollection, OutputFormat, Severity


def print_error_messages(
    output_format: Literal[OutputFormat.TXT, OutputFormat.JSON],
    error_message_collection: ErrorMessageCollection,
):
    if output_format == OutputFormat.JSON:
        errors = [
            error.__dict__ for error in error_message_collection.error_messages
        ]
        print()
        print(
            json.dumps(
                {
                    'error_messages': errors,
                    'total_errors': error_message_collection.total_errors,
                    'total_warnings': error_message_collection.total_warnings,
                },
                indent=2,
            )
        )
    else:
        for error in error_message_collection.error_messages:
            print()
            if error.severity == Severity.ERROR:
                print(f'[red bold]ERROR[/red bold]')
            else:
                print(f'[yellow bold]WARN[/yellow bold]')
            print(f'[bold]Rule:[/bold] {error.rule}')
            print(f'[bold]Context:[/bold] {error.context}')
            print(f'[bold]Messages:[/bold]')
            for message in error.messages:
                print(f'- {message}')
            if len(error.documentations) > 0:
                print(f'[bold]Documentations:[/bold]')
                for doc in error.documentations:
                    print(f'- {doc}')
        print()
        print(
            f'[red bold]Total errors: {error_message_collection.total_errors}[/red bold]'
        )
        print(
            f'[yellow bold]Total warnings: {error_message_collection.total_warnings}[/yellow bold]'
        )
