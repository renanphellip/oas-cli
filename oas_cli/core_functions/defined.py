from typing import Any, Dict, List


def defined(
    context: str = '',
    target_value: Dict[str, Any] = {},
    function_options: Dict[str, str] = {},
    field_name: str = '',
    verbose = False
) -> List[str]:
    if target_value.get(field_name) is None:
        return [f'{context}.{field_name} must not be null.']
    return []
