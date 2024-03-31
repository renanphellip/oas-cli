from typing import Any, Dict, List


def truthy(
    context: str, target_value: Any, function_options: Dict[str, str]
) -> List[str]:
    falsy_values = (False, '', 0, None)
    if target_value in falsy_values:
        return [f'{context} não deve ser: {falsy_values}']
    return []