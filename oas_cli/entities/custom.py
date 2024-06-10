from enum import Enum
from typing import Any, Dict, List, Union

from pydantic.dataclasses import dataclass

from oas_cli.entities.rulesets import RuleThen, Severity


@dataclass
class CustomRuleThen:
    then: Union[RuleThen, List[RuleThen]]

    @property
    def fields(self) -> List[dict[str, str]]:
        if isinstance(self.then, list):
            return [
                {'field': item.field, 'function': item.function}
                for item in self.then
            ]
        return []

    @property
    def field(self) -> str:
        if isinstance(self.then, RuleThen):
            return self.then.field
        return ''

    @property
    def function(self) -> str:
        if isinstance(self.then, RuleThen):
            return self.then.function
        return ''

    @property
    def function_options(self) -> Dict[str, Any]:
        if isinstance(self.then, RuleThen):
            return self.then.functionOptions
        return {}


@dataclass
class CustomRule:
    name: str
    description: str
    message: Union[str, List[str]]
    documentation: Union[str, List[str]]
    severity: Severity
    resolved: bool
    _given: Union[str, List[str]]
    then: CustomRuleThen

    def __post_init__(self):
        if isinstance(self._given, str):
            self.__given = self.__process_given(self._given)
        else:
            self.__given = [
                self.__process_given(context) for context in self._given
            ]

    def __process_given(self, given_string: str) -> str:
        paths = given_string.split('.')
        processed_paths = []
        for path in paths:
            if (
                '/' in path
                and not path.startswith(('"', "'"))
                and not path.endswith(('"', "'"))
            ):
                processed_paths.append(f'"{path}"')
            else:
                processed_paths.append(path)
        return '.'.join(processed_paths)

    @property
    def given(self) -> Union[str, List[str]]:
        return self.__given


@dataclass
class ErrorMessage:
    rule: str
    context: str
    severity: Severity
    messages: List[str]
    documentations: List[str]


@dataclass
class ErrorMessageCollection:
    error_messages: List[ErrorMessage]

    @property
    def total_errors(self) -> int:
        return sum(
            1
            for error in self.error_messages
            if error.severity == Severity.ERROR
        )

    @property
    def total_warnings(self) -> int:
        return sum(
            1
            for error in self.error_messages
            if error.severity == Severity.WARN
        )


class OutputFormat(str, Enum):
    TXT = 'text'
    JSON = 'json'
    NONE = 'none'

    def __str__(self):
        return self.value


@dataclass
class JSONPathResult:
    context: str
    target_value: Any
