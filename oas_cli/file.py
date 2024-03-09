import json
import os
import sys
from typing import Any, Dict

import yaml
from rich import print

from oas_cli.entities import ErrorMessageCollection


def validate_file_extension(
    file_path: str, supported_extensions: tuple[str]
) -> str:
    if not file_path.lower().endswith(supported_extensions):
        print(
            f'[red]The file path "{file_path}" does not have a valid extension: {supported_extensions}[/red]'
        )
        sys.exit(1)
    return file_path


def validate_file_path(
    file_path: str, supported_extensions: tuple[str]
) -> str:
    validate_file_extension(file_path, supported_extensions)
    if not os.path.exists(file_path):
        print(f'[red]The file path "{file_path}" was not found.[/red]')
        sys.exit(1)
    return file_path


def read_file(file_path: str) -> Dict[str, Any]:
    try:
        absolute_file_path = os.path.abspath(file_path.strip())
        if absolute_file_path.endswith('.json'):
            with open(absolute_file_path, 'r') as file:
                return json.load(file)
        else:
            with open(absolute_file_path, 'r') as file:
                return yaml.safe_load(file)
    except Exception as error:
        print(
            f'[red]Failed to read the file "{absolute_file_path}": {error}[/red]'
        )
        sys.exit(1)


def write_file(output_path: str, data: Any) -> str:
    try:
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        absolute_output_path = os.path.abspath(output_path.strip())
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
        print(
            f'[red]Failed to write the file "{absolute_output_path}": {error}[/red]'
        )
        sys.exit(1)
