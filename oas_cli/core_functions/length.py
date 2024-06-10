from typing import Any, Dict, List


def length(
    context: str = '',
    target_value: Dict[str, Any] = {},
    function_options: Dict[str, str] = {},
    field_name: str = '',
    verbose = False
) -> List[str]:
    max_length = function_options.get('max')
    min_length = function_options.get('min')
    if isinstance(min_length, int) and isinstance(max_length, int):
        min_length = int(min_length)
        max_length = int(max_length)
        field_target_value = target_value.get(field_name)
        if isinstance(field_target_value, (str, list, dict)):
            if (
                len(field_target_value) > max_length
                or len(field_target_value) < min_length
            ):
                return [
                    f'The length of {context}.{field_name} must be between {min_length} and {max_length}.'
                ]
        if isinstance(field_target_value, int):
            if (
                field_target_value > max_length
                or field_target_value < min_length
            ):
                return [
                    f'The value of {context}.{field_name} must be between {min_length} and {max_length}.'
                ]
    return []
