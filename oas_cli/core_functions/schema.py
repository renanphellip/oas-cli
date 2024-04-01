from typing import Any, Dict, List

import jsonschema


def schema(
    context: str = '',
    target_value: Dict[str, Any] = {},
    function_options: Dict[str, str] = {},
    field_name: str = '',
) -> List[str]:
    try:
        expected_schema = function_options.get('schema')
        field_target_value = target_value.get(field_name)
        jsonschema.validate(
            instance=field_target_value, schema=expected_schema
        )
        return []
    except Exception:
        return [
            f'{context}.{field_name} does not meet the expected schema: {expected_schema}'
        ]
