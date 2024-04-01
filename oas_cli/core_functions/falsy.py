from typing import Any, Dict, List


def falsy(
    context: str, target_value: Dict[str, Any], field_name: str
) -> List[str]:
    falsy_values = (False, '', 0, None)
    if target_value.get(field_name) not in falsy_values:
        return [f'{context}.{field_name} must be: {falsy_values}']
    return []