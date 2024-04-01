from dataclasses import dataclass
from enum import Enum
from typing import List, Union


@dataclass
class RuleThen:
    then: Union[List[dict[str, str]], dict[str, str]]

    @property
    def fields(self) -> List[dict[str, str]]:
        if isinstance(self.then, list):
            return [
                {'field': item.get('field'), 'function': item.get('function')}
                for item in self.then
            ]
        return []

    @property
    def field(self) -> str:
        if isinstance(self.then, dict):
            return self.then.get('field', '')
        return ''

    @property
    def function(self) -> str:
        if isinstance(self.then, dict):
            return self.then.get('function', '')
        return ''

    @property
    def functionOptions(self) -> dict[str, str]:
        if isinstance(self.then, dict):
            return self.then.get('functionOptions', {})
        return {}


class Severity(str, Enum):
    ERROR = 'error'
    WARN = 'warn'

    def __str__(self):
        return self.value


@dataclass
class Rule:
    name: str
    description: str
    message: Union[str, List[str]]
    documentation: Union[str, List[str]]
    severity: str
    _given: Union[str, List[str]]
    then: str

    def __post_init__(self):
        if isinstance(self._given, str):
            self.__given = self.process_given(self._given)
        else:
            self.__given = [
                self.process_given(context) for context in self._given
            ]

    def process_given(self, given_str: str) -> str:
        paths = given_str.split('.')
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
