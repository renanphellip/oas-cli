import json
import os
import sys
from typing import Any, Callable, Dict, List

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

    def __get_jsonpath_results(self, jsonpath_pattern: str, data: Dict[str, Any]) -> List[JSONPathResult]:
        try:
            root_string = '' if jsonpath_pattern == '$' else '$.'
            naming_filter = jsonpath_pattern.endswith('~')
            jsonpath_pattern = jsonpath_pattern[:-1] if naming_filter else jsonpath_pattern
            pattern = parse(jsonpath_pattern)
            results = [
                JSONPathResult(
                    context=root_string + str(match.full_path),
                    target_value=str(match.path) if naming_filter else match.value
                )
                for match in pattern.find(data)
            ]
            return results
        except Exception as error:
            self.__console.print(
                f'[red]Failed to parse JSONPath "{escape(jsonpath_pattern)}": {escape(str(error))}[/red]'
            )
            sys.exit(1)

    def __replace_messages(self, messages: List[str], old_value: str, new_value: str) -> List[str]:
        return [message.replace(old_value, new_value) for message in messages]

    def __create_error_messages(self, function_messages: List[str], rule: CustomRule, jsonpath_result: JSONPathResult) -> List[str]:
        if not rule.message or '{{error}}' in rule.message:
            errors = function_messages
        elif '{{description}}' in rule.message:
            errors = [rule.description]
        else:
            errors = rule.message if isinstance(rule.message, list) else [rule.message]
        errors = self.__replace_messages(errors, '{{path}}', jsonpath_result.context)
        property_name = jsonpath_result.context.split('.')[-1]
        errors = self.__replace_messages(errors, '{{property}}', property_name)
        target_value = json.dumps(jsonpath_result.target_value) if isinstance(jsonpath_result.target_value, object) else jsonpath_result.target_value
        errors = self.__replace_messages(errors, '{{value}}', target_value)
        return errors

    def __create_error_message_instance(self, rule: CustomRule, jsonpath_result: JSONPathResult, errors: List[str]) -> ErrorMessage:
        if isinstance(rule.documentation, list):
            docs = rule.documentation
        elif isinstance(rule.documentation, str) and rule.documentation:
            docs = [rule.documentation]
        else:
            docs = []
        return ErrorMessage(
            rule=rule.name,
            context=jsonpath_result.context,
            severity=rule.severity,
            messages=errors,
            documentations=docs
        )
    
    def __run_function(self, rule: CustomRule, rule_function: Callable, jsonpath_results: List[JSONPathResult], field: str) -> List[ErrorMessage]:
        error_messages: List[ErrorMessage] = []
        for result in jsonpath_results:
            function_messages = rule_function(result.context, result.target_value, rule.then.function_options, field)
            if function_messages:
                errors = self.__create_error_messages(function_messages, rule, result)
                error_messages.append(self.__create_error_message_instance(rule, result, errors))
        return error_messages

    def __load_contract_data(self, contract_path: str, resolve_contract: bool) -> Dict[str, Any]:
        if resolve_contract:
            resolver = Resolver()
            return resolver.resolve(contract_path)
        else:
            return read_file(contract_path)

    def __load_functions(self, custom_functions_path: str) -> Dict[str, Callable]:
        core_functions_dir = os.path.abspath('oas_cli/core_functions')
        custom_functions_dir = os.path.abspath(custom_functions_path)
        core_functions = get_functions(core_functions_dir)
        custom_functions = get_functions(custom_functions_dir)

        functions = core_functions.copy()
        for key, value in custom_functions.items():
            if key not in core_functions:
                functions[key] = value
            else:
                self.__console.print(f'[yellow]Custom function "{escape(key)}" not loaded as a core function with the same name exists.[/yellow]')
        return functions

    def __get_jsonpath_results_from_rule(self, rule: CustomRule, contract_data: Dict[str, Any]) -> List[JSONPathResult]:
        if isinstance(rule.given, list):
            results: List[JSONPathResult] = []
            for context in rule.given:
                results.extend(self.__get_jsonpath_results(context, contract_data))
            return results
        else:
            return self.__get_jsonpath_results(rule.given, contract_data)

    def __process_rule(self, rule: CustomRule, functions: Dict[str, Callable], jsonpath_results: List[JSONPathResult]) -> List[ErrorMessage]:
        error_messages: List[ErrorMessage] = []
        fields = rule.then.fields
        field = rule.then.field
        for target_field in fields or [field]:
            if isinstance(target_field, dict):
                function_name = target_field.get('function', rule.then.function)
            elif field:
                function_name = field
            else:
                function_name = rule.then.function
            rule_function = functions.get(function_name)
            list_error_messages = self.__run_function(rule, rule_function, jsonpath_results, target_field)
            error_messages.extend(list_error_messages)
        return error_messages

    def validate(self, contract_path: str, ruleset_path: str, custom_functions_path: str, resolve_contract: bool = False) -> ErrorMessageCollection:
        try:
            contract_data = self.__load_contract_data(contract_path, resolve_contract)
            rules = get_rules(ruleset_path)
            functions = self.__load_functions(custom_functions_path)

            validate_functions(rules, functions)

            error_messages = []

            for rule in rules:
                jsonpath_results = self.__get_jsonpath_results_from_rule(rule, contract_data)
                error_messages.extend(self.__process_rule(rule, functions, jsonpath_results))

            return ErrorMessageCollection(error_messages)

        except Exception as error:
            self.__console.print(f'[red]Failed to validate the contract: {escape(str(error))}[/red]')
            sys.exit(1)
