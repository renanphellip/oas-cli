from typing import Any, Dict, List


def xor(
    context: str = '',
    target_value: Dict[str, Any] = {},
    function_options: Dict[str, str] = {},
    field_name: str = '',
    verbose = False
) -> List[str]:
    properties = function_options.get('properties')
    properties_found = sum(
        1 for property in properties if property in target_value
    )
    if properties_found != 1:
        return [
            f'{context} must have only one of these properties defined: {properties}'
        ]
    return []
