import sys
from typing import Any, Dict, List

from pydantic import ValidationError
from rich.console import Console
from rich.markup import escape

from oas_cli.entities.custom import CustomRule, CustomRuleThen
from oas_cli.entities.rulesets import Rulesets
from oas_cli.file import read_file


def get_rules(ruleset_path: str) -> List[CustomRule]:
    console = Console(highlight=False)
    try:
        rulesets_data: Dict[str, Any] = read_file(ruleset_path)
        rulesets = Rulesets.model_validate(rulesets_data)
        rules: List[CustomRule] = []
        for rule_name, rule in rulesets.rules.items():
            rules.append(
                CustomRule(
                    name=rule_name,
                    description=rule.description,
                    message=rule.message,
                    documentation=rule.documentation,
                    severity=rule.severity,
                    _given=rule.given,
                    then=CustomRuleThen(rule.then)
                )
            )
        return rules
    except ValidationError as error:
        console.print(f'[red]Invalid rulesets schema: {escape(str(error))}[/red]')
        sys.exit(1)
