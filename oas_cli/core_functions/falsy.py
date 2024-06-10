from typing import Any, Dict, List


def falsy(
    context: str = '',
    target_value: Dict[str, Any] = {},
    function_options: Dict[str, str] = {},
    field_name: str = '',
    verbose = False
) -> List[str]:
    falsy_values = (False, '', 0, None)
    if target_value.get(field_name) not in falsy_values:
        return [
            f'{context}.{field_name} must be: empty string, 0, false, null'
        ]
    return []
