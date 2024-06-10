from typing import Any, Dict, List


def enumeration(
    context: str = '',
    target_value: Dict[str, Any] = {},
    function_options: Dict[str, str] = {},
    field_name: str = '',
    verbose = False
) -> List[str]:
    possible_values = function_options.get('values')
    field_target_value = target_value.get(field_name)
    if isinstance(possible_values, list):
        if field_target_value not in possible_values:
            return [f'{context}.{field_name} must be: {possible_values}']
    return []
