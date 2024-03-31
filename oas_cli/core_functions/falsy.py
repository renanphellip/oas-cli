from typing import Any, Dict, List


def falsy(
    context: str, target_value: Any, function_options: Dict[str, str]
) -> List[str]:
    falsy_values = (False, '', 0, None)
    if target_value not in falsy_values:
        return [f'{context} deve ser: {falsy_values}']
    return []