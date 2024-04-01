import json
from typing import Literal

from rich.console import Console
from rich.markup import escape

from oas_cli.entities import ErrorMessageCollection, OutputFormat, Severity


def print_error_messages(
    output_format: Literal[OutputFormat.TXT, OutputFormat.JSON],
    error_message_collection: ErrorMessageCollection,
):
    console = Console(highlight=False)
    if output_format == OutputFormat.JSON:
        errors = [
            error.__dict__ for error in error_message_collection.error_messages
        ]
        console.print()
        console.print(
            escape(
                json.dumps(
                    {
                        'error_messages': errors,
                        'total_errors': error_message_collection.total_errors,
                        'total_warnings': error_message_collection.total_warnings,
                    },
                    indent=2,
                )
            )
        )
    else:
        for error in error_message_collection.error_messages:
            console.print()
            if error.severity == Severity.ERROR:
                console.print(f'[red bold]ERROR[/red bold]')
            else:
                console.print(f'[yellow bold]WARN[/yellow bold]')
            console.print(f'[bold]Rule:[/bold] {escape(error.rule)}')
            console.print(f'[bold]Context:[/bold] {escape(error.context)}')
            console.print(f'[bold]Messages:[/bold]')
            for message in error.messages:
                console.print(f'- {escape(message)}')
            if len(error.documentations) > 0:
                console.print(f'[bold]Documentations:[/bold]')
                for doc in error.documentations:
                    console.print(f'- {escape(doc)}')
        console.print()
        console.print(
            f'[red bold]Total errors: {error_message_collection.total_errors}[/red bold]'
        )
        console.print(
            f'[yellow bold]Total warnings: {error_message_collection.total_warnings}[/yellow bold]'
        )
