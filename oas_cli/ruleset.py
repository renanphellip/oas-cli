import json
import sys
from typing import Any, List, Literal

import jsonschema
from rich import print

from oas_cli.entities import Rule, RuleThen, Severity
from oas_cli.file import read_file
from oas_cli.ruleset_schema import ruleset_schema


def validate_ruleset_integrity(ruleset_path: str) -> Literal[True]:
    ruleset_data: dict = read_file(ruleset_path)
    ruleset_json_data = json.loads(json.dumps(ruleset_data))
    try:
        jsonschema.validate(instance=ruleset_json_data, schema=ruleset_schema)
        return True
    except Exception as error:
        print(f'[red]Invalid ruleset schema: {error}[/red]')
        sys.exit(1)


def get_ruleset(ruleset_path: str) -> List[Rule]:
    ruleset_data: dict[str, Any] = read_file(ruleset_path)
    rules: dict[str, Any] = ruleset_data.get('rules')
    ruleset: List[Rule] = []
    for rule_name in ruleset_data.get('rules'):
        rule_def: dict[str, Any] = rules.get(rule_name)
        rule_severity = Severity.WARN
        if rule_def.get('severity') == 'error':
            rule_severity = Severity.ERROR
        ruleset.append(
            Rule(
                name=rule_name,
                description=rule_def.get('description'),
                message=rule_def.get('message'),
                documentation=rule_def.get('documentation', ''),
                severity=rule_severity,
                _given=rule_def.get('given'),
                then=RuleThen(rule_def.get('then')),
            )
        )
    return ruleset
