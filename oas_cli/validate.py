import os
import sys
from typing import List

from jsonpath_ng import parse
from rich import print

from oas_cli.custom_function import (get_custom_functions,
                                     validate_custom_functions)
from oas_cli.entities import ErrorMessage, ErrorMessageCollection
from oas_cli.file import read_file
from oas_cli.resolve import resolve
from oas_cli.ruleset import get_ruleset, validate_ruleset_integrity


def get_jsonpath_results(jsonpath_pattern: str, data: object):
    pattern = parse(jsonpath_pattern)
    results = [
        {'context': '$.' + str(match.full_path), 'target_value': match.value}
        for match in pattern.find(data)
    ]
    return results


def validate(
    contract_path: str, ruleset_path: str, resolve_contract: bool = False
) -> ErrorMessageCollection:
    try:
        if resolve_contract:
            contract_data = resolve(contract_path)
        else:
            contract_data = read_file(contract_path)

        validate_ruleset_integrity(ruleset_path)

        ruleset = get_ruleset(ruleset_path)

        functions_directory = os.path.abspath('oas_cli/functions')
        custom_functions = get_custom_functions(functions_directory)
        validate_custom_functions(ruleset, custom_functions)

        error_messages: List[ErrorMessage] = []

        for rule in ruleset:
            results = []
            if isinstance(rule.given, list):
                for context in rule.given:
                    results.extend(
                        get_jsonpath_results(context, contract_data)
                    )
            else:
                context = rule.given
                results = get_jsonpath_results(context, contract_data)

            function_name = rule.then.function
            function_options = rule.then.functionOptions
            custom_function = custom_functions[function_name]

            for result in results:
                messages: List[str] = custom_function(
                    result.get('context'),
                    result.get('target_value'),
                    function_options,
                )

                if len(messages) > 0:
                    errors: List[str] = []
                    if '{{error}}' in rule.message:
                        errors.extend(messages)
                    else:
                        if isinstance(rule.message, list):
                            errors.extend(rule.message)
                        else:
                            errors.append(rule.message)

                    docs: List[str] = []
                    if len(rule.documentation) > 0:
                        if isinstance(rule.documentation, list):
                            docs.extend(rule.documentation)
                        else:
                            docs.append(rule.documentation)

                    error_messages.append(
                        ErrorMessage(
                            rule=rule.name,
                            context=result.get('context'),
                            severity=rule.severity,
                            messages=errors,
                            documentations=docs,
                        )
                    )

        return ErrorMessageCollection(error_messages)

    except Exception as error:
        print(f'[red]Failed to validate the contract: {error}[/red]')
        sys.exit(1)
