from dataclasses import dataclass
from enum import Enum
from typing import List, Union


@dataclass
class RuleThen:
    then: dict[str, str]

    @property
    def function(self) -> str:
        return self.then.get('function')

    @property
    def functionOptions(self) -> dict[str, str]:
        return self.then.get('functionOptions')


class Severity(str, Enum):
    ERROR = 'error'
    WARN = 'warn'

    def __str__(self):
        return self.value


@dataclass
class Rule:
    name: str
    description: str
    message: Union[str | List[str]]
    documentation: Union[str | List[str]]
    severity: Severity
    given: Union[str | List[str]]
    then: RuleThen


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
