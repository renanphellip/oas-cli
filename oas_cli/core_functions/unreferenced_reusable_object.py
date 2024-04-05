from typing import Any, Dict, List


def ref_exists(data: Any, reusable_objects_location: str) -> bool:
    if isinstance(data, dict):
        for key, value in data.items():
            if key == '$ref' and isinstance(value, str):
                if value == reusable_objects_location:
                    return True
            if isinstance(value, dict):
                if ref_exists(value, reusable_objects_location):
                    return True
            elif isinstance(value, list):
                for item in value:
                    if ref_exists(item, reusable_objects_location):
                        return True
    if isinstance(data, list):
        for item in data:
            if ref_exists(item, reusable_objects_location):
                return True
    if isinstance(data, str):
        if data == reusable_objects_location:
            return True
    return False


def unreferencedReusableObject(
    context: str = '',
    target_value: Any = {},
    function_options: Dict[str, str] = {},
    field_name: str = '',
) -> List[str]:
    reusable_objects_location = function_options.get('reusableObjectsLocation')
    if not ref_exists(target_value, reusable_objects_location):
        return [
            f'No reference to {reusable_objects_location} was found in {context}.'
        ]
    return []
