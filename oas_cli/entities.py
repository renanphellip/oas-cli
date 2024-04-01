from dataclasses import dataclass
from enum import Enum
from typing import List, Union


@dataclass
class RuleThen:
    then: Union[List[dict[str, str]], dict[str, str]]

    @property
    def fields(self) -> List[dict[str, str]]:
        fields = []
        if isinstance(self.then, list):
            for item in self.then:
                fields.append({
                    'field': item.get('field'),
                    'function': item.get('function')
                })
        return fields

    @property
    def function(self) -> str:
        if isinstance(self.then, dict):
            return self.then.get('function')
        return None

    @property
    def functionOptions(self) -> dict[str, str]:
        if isinstance(self.then, dict):
            return self.then.get('functionOptions')
        return None


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
    severity: Severity
    _given: Union[str, List[str]]
    then: RuleThen

    @property
    def given(self) -> Union[str, List[str]]:
        if isinstance(self._given, str):
            return '.'.join([f'"{path}"' if '/' in path and not path.startswith(('"', "'")) and not path.endswith(('"', "'")) else path for path in self._given.split('.')])
        else:
            return ['.'.join([f'"{path}"' if '/' in path and not path.startswith(('"', "'")) and not path.endswith(('"', "'")) else path for path in context.split('.')]) for context in self._given]

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
        total_errors = 0
        for error in self.error_messages:
            if error.severity == Severity.ERROR:
                total_errors += 1
        return total_errors

    @property
    def total_warnings(self) -> int:
        total_warnings = 0
        for error in self.error_messages:
            if error.severity == Severity.WARN:
                total_warnings += 1
        return total_warnings


class OutputFormat(str, Enum):
    TXT = 'text'
    JSON = 'json'
    NONE = 'none'

    def __str__(self):
        return self.value
