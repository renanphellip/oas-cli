#!/usr/bin/env python3

import typer

from oas_cli.commands.version import version
from oas_cli.commands.resolve import resolve
from oas_cli.commands.validate import validate


cli = typer.Typer(help='OpenAPI Specification CLI', no_args_is_help=True)
cli.command(help='Show OAS CLI version')(version)
cli.command(help='Resolve YAML external references')(resolve)
cli.command(help='Validate rulesets to OpenAPI document')(validate)

if __name__ == '__main__':
    cli()
