import importlib.util
import os
import sys
from typing import Dict, List, Literal

from rich import print

from oas_cli.entities import Rule


def get_functions(functions_path: str):
    if not os.path.isdir(functions_path):
        print(
            f'[red]The path "{functions_path}" is not a valid directory.[/red]'
        )
        sys.exit(1)
    try:
        functions = {}
        for file_name in os.listdir(functions_path):
            if file_name.endswith('.py'):
                module_path = os.path.join(functions_path, file_name)
                module_name = os.path.splitext(file_name)[0]
                spec = importlib.util.spec_from_file_location(
                    module_name, module_path
                )
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                for name in dir(module):
                    attribute = getattr(module, name)

                    if callable(attribute) and not name.startswith('_'):
                        functions[name] = attribute
        return functions
    except Exception as error:
        print(
            f'[red]Failed to load functions from "{functions_path}": {error}[/red]'
        )
        sys.exit(1)


def validate_functions(ruleset: List[Rule], functions: Dict) -> Literal[True]:
    for rule in ruleset:
        if len(rule.then.fields) > 0:
            fields = rule.then.fields
            for field in fields:
                function_name = field.get('function')
                if function_name not in functions:
                    print(
                        f'[red]The function "{function_name}" was not found for rule "{rule.name}".[/red]'
                    )
                    sys.exit(1)
        else:
            function_name = rule.then.function
            if function_name not in functions:
                print(
                    f'[red]The function "{function_name}" was not found for rule "{rule.name}".[/red]'
                )
                sys.exit(1)
    return True
