import os
import sys
from typing import Callable, List

from jsonpath_ng import parse
from rich.console import Console
from rich.markup import escape

from oas_cli.entities.custom import (CustomRule, ErrorMessage,
                                     ErrorMessageCollection, JSONPathResult)
from oas_cli.file import read_file
from oas_cli.function import get_functions, validate_functions
from oas_cli.resolver import Resolver
from oas_cli.rulesets import get_rules


class Validator:
    def __init__(self):
        self.__console = Console(highlight=False)

    def __get_jsonpath_results(self, jsonpath_pattern: str, data: object) -> List[JSONPathResult]:
        try:
            root_string = '$.'
            if jsonpath_pattern == '$':
                root_string = ''
            pattern = parse(jsonpath_pattern)
            results = [
                JSONPathResult(
                    context=root_string + str(match.full_path),
                    target_value=match.value
                )
                for match in pattern.find(data)
            ]
            return results
        except Exception as error:
            self.__console.print(
                f'[red]Failed to parse JSONPath "{escape(jsonpath_pattern)}": {escape(str(error))}[/red]'
            )
            sys.exit(1)

    def __run_function(self, rule: CustomRule, rule_function: Callable, jsonpath_results: List[JSONPathResult], field: str ) -> List[ErrorMessage]:
        error_messages: List[ErrorMessage] = []
        for result in jsonpath_results:
            function_messages: List[str] = rule_function(
                result.context,
                result.target_value,
                rule.then.function_options,
                field,
            )
            if len(function_messages) > 0:
                errors: List[str] = []
                if len(rule.message) == 0 or '{{error}}' in rule.message:
                    errors.extend(function_messages)
                elif '{{description}}' in rule.message:
                    errors.append(rule.description)
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
                        context=result.context,
                        severity=rule.severity,
                        messages=errors,
                        documentations=docs,
                    )
                )
        return error_messages

    def validate(
        self, contract_path: str, ruleset_path: str, resolve_contract: bool = False
    ) -> ErrorMessageCollection:
        try:
            if resolve_contract:
                resolver = Resolver()
                contract_data = resolver.resolve(contract_path)
            else:
                contract_data = read_file(contract_path)

            rules = get_rules(ruleset_path)

            core_functions_dir = os.path.abspath('oas_cli/core_functions')
            core_functions = get_functions(core_functions_dir)

            custom_functions_dir = os.path.abspath('oas_cli/custom_functions')
            custom_functions = get_functions(custom_functions_dir)

            functions = core_functions.copy()
            for key, value in custom_functions.items():
                if key not in core_functions:
                    functions[key] = value
                else:
                    self.__console.print(f'[yellow]The custom function "{escape(key)}" will not be load because a core function with this name already exists.[/yellow]')

            validate_functions(rules, functions)

            error_messages: List[ErrorMessage] = []

            for rule in rules:
                jsonpath_results = []
                if isinstance(rule.given, list):
                    for context in rule.given:
                        jsonpath_results.extend(
                            self.__get_jsonpath_results(context, contract_data)
                        )
                else:
                    context = rule.given
                    jsonpath_results = self.__get_jsonpath_results(context, contract_data)

                fields = rule.then.fields
                field = rule.then.field
                function_name = rule.then.function

                if len(fields) > 0:
                    for field in fields:
                        function_name = field.get('function')
                        rule_function = functions.get(function_name)
                        list_error_messages = self.__run_function(rule, rule_function, jsonpath_results, field)
                        error_messages.extend(list_error_messages)
                else:
                    rule_function = functions.get(function_name)
                    list_error_messages = self.__run_function(rule, rule_function, jsonpath_results, field)
                    error_messages.extend(list_error_messages)

            return ErrorMessageCollection(error_messages)

        except Exception as error:
            self.__console.print(f'[red]Failed to validate the contract: {escape(str(error))}[/red]')
            sys.exit(1)
