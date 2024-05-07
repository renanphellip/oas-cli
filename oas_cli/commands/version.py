import sys
from typing import Literal

from rich import print

from oas_cli.file import (
    read_file
)


def version() -> Literal[True]:
    try:
        data = read_file('pyproject.toml')
        version = data['tool']['poetry']['version']
        print(f'OAS CLI version: {version}')
        return True
    except:
        print('[red]OAS CLI version was not specified.[/red]')
        sys.exit(1)
