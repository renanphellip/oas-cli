import json
import os
import sys
from typing import Any

import yaml
from rich import print


def read_file(file_path: str) -> Any:
    try:
        absolute_file_path = os.path.abspath(file_path.strip())
        if absolute_file_path.endswith('.yaml') or absolute_file_path.endswith(
            'yml'
        ):
            with open(absolute_file_path, 'r') as file:
                return yaml.safe_load(file)
        elif absolute_file_path.endswith('.json'):
            with open(absolute_file_path, 'r') as file:
                return json.load(file)
        else:
            print(
                '[red]Invalid file extension. The supported extensions are: .yaml, .yml, .json[/red]'
            )
            sys.exit(1)
    except Exception as error:
        print(
            f'[red]Failed to read the file "{absolute_file_path}": {error}[/red]'
        )
        sys.exit(1)


def write_file(output_path: str, data: Any) -> str:
    try:
        absolute_output_path = os.path.abspath(output_path.strip())
        if absolute_output_path.endswith(
            '.yaml'
        ) or absolute_output_path.endswith('yml'):
            with open(absolute_output_path, 'w') as file:
                yaml.safe_dump(data, file, sort_keys=False)
                return absolute_output_path
        elif absolute_output_path.endswith('.json'):
            with open(absolute_output_path, 'w') as file:
                json.dump(data, file, sort_keys=False)
                return absolute_output_path
        else:
            print(
                '[red]Invalid file extension. The supported extensions are: .yaml, .yml, .json[/red]'
            )
            sys.exit(1)
    except Exception as error:
        print(
            f'[red]Failed to write the file "{absolute_output_path}": {error}[/red]'
        )
        sys.exit(1)
