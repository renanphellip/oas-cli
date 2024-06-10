import json
import os
import sys
from typing import Any, Dict

import yaml
from rich.console import Console
import tomli

from oas_cli.entities.custom import ErrorMessageCollection


console = Console(highlight=False)


def validate_file_extension(
    file_path: str, supported_extensions: tuple[str], verbose=False
) -> str:
    if verbose:
        console.print(f'The "[blue]{file_path}[/blue]" file has a valid extension.')
    if not file_path.lower().endswith(supported_extensions):
        console.print(
            f'[red]The file path "{file_path}" does not have a valid extension: {supported_extensions}[/red]'
        )
        sys.exit(1)
    return file_path


def validate_file_path(
    file_path: str, supported_extensions: tuple[str], verbose=False
) -> str:
    validate_file_extension(file_path, supported_extensions, verbose)
    if verbose:
        console.print(f'The "[blue]{file_path}[/blue]" file path exists as expected.')
    if not os.path.exists(file_path):
        console.print(f'[red]The file path "{file_path}" was not found.[/red]')
        sys.exit(1)
    return file_path


def read_file(file_path: str, verbose=False) -> Dict[str, Any]:
    try:
        absolute_file_path = os.path.abspath(file_path.strip())
        if verbose:
            console.print(f'The absolute file path is: [blue]{absolute_file_path}[/blue]')
            console.print(f'Loading "[blue]{absolute_file_path}[/blue]"...')
        if absolute_file_path.endswith('.toml'):
            with open(absolute_file_path, 'rb') as file:
                return tomli.load(file)
        elif absolute_file_path.endswith('.json'):
            with open(absolute_file_path, 'r') as file:
                return json.load(file)
        else:
            with open(absolute_file_path, 'r') as file:
                return yaml.safe_load(file)
    except Exception as error:
        console.print(
            f'[red]Failed to read the file "{absolute_file_path}": {error}[/red]'
        )
        sys.exit(1)


def write_file(output_path: str, data: Any, verbose=False) -> str:
    try:
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            if verbose:
                console.print(f'The path "[blue]{output_dir}[/blue]" not exists. Creating...')
            os.makedirs(output_dir)
        absolute_output_path = os.path.abspath(output_path.strip())
        if verbose:
            console.print(f'The absolute output path is: [blue]{absolute_output_path}[/blue]')
            console.print(f'Creating "[blue]{absolute_output_path}[/blue]"...')
        if absolute_output_path.endswith('.json'):
            with open(absolute_output_path, 'w', encoding='utf-8') as file:
                if isinstance(data, ErrorMessageCollection):
                    errors = [error.__dict__ for error in data.error_messages]
                    json.dump(
                        {
                            'error_messages': errors,
                            'total_errors': data.total_errors,
                            'total_warnings': data.total_warnings,
                        },
                        file,
                    )
                else:
                    json.dump(data, file, sort_keys=False)
        elif absolute_output_path.endswith(('.yml', 'yaml')):
            with open(absolute_output_path, 'w', encoding='utf-8') as file:
                yaml.safe_dump(data, file, sort_keys=False)
        else:
            if isinstance(data, ErrorMessageCollection):
                with open(absolute_output_path, 'w', encoding='utf-8') as file:
                    for error in data.error_messages:
                        file.write(f'{error.severity.upper()}\n')
                        file.write(f'Rule: {error.rule}\n')
                        file.write(f'Context: {error.context}\n')
                        file.write(f'Messages:\n')
                        for message in error.messages:
                            file.write(f'- {message}\n')
                        if len(error.documentations) > 0:
                            file.write(f'Documentations:\n')
                            for doc in error.documentations:
                                file.write(f'- {doc}\n')
                        file.write('\n')
                    file.write(f'Total errors: {data.total_errors}\n')
                    file.write(f'Total warnings: {data.total_warnings}\n')
        return absolute_output_path
    except Exception as error:
        console.print(
            f'[red]Failed to write the file "{absolute_output_path}": {error}[/red]'
        )
        sys.exit(1)
