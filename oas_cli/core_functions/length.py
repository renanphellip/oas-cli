from typing import Any, Dict, List


def length(
    context: str = '',
    target_value: Dict[str, Any] = {},
    function_options: Dict[str, str] = {},
    field_name: str = '',
) -> List[str]:
    max_length = function_options.get('max')
    min_length = function_options.get('min')
    field_target_value = target_value.get(field_name)
    if isinstance(field_target_value, (str, list, dict, int)):
        if (
            len(field_target_value) > max_length
            or len(field_target_value) < min_length
        ):
            return [
                f'The length of {context}.{field_name} must be between {min_length} and {max_length}.'
            ]
    return []