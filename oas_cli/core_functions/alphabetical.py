from typing import Any, Dict, List


def alphabetical(
    context: str = '',
    target_value: Dict[str, Any] = {},
    function_options: Dict[str, str] = {},
    field_name: str = '',
    verbose = False
) -> List[str]:
    field_target_value = target_value.get(field_name)
    keyed_by = function_options.get('keyedBy')
    if isinstance(field_target_value, list) and keyed_by:
        keys = [item.get(keyed_by) for item in field_target_value if keyed_by in item]
        if keys != sorted(keys):
            return [f'{context} should have alphabetical {field_name} by {keyed_by}.']
    return []
