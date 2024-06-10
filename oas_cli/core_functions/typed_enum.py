from typing import Dict, List, Union


def typedEnum(
    context: str = '',
    target_value: Union[str, int, float, bool] = '',
    function_options: Dict[str, str] = {},
    field_name: str = '',
    verbose = False
) -> List[str]:
    opt_enum = function_options.get('enum')
    opt_type = function_options.get('type')
    data_types = {
        'string': str,
        'integer': int,
        'number': (int, float),
        'boolean': bool,
    }
    messages = []
    if isinstance(opt_enum, list):
        if opt_type in data_types:
            for item in opt_enum:
                if not isinstance(item, data_types.get(opt_type)):
                    messages.append(f'The enum value {item} must be of type {opt_type}.')
            if not isinstance(target_value, data_types.get(opt_type)):
                messages.append(f'The value {target_value} in {context} must be of type {opt_type}.')
        if target_value not in opt_enum:
            messages.append(f'{context} must be: {opt_enum}')
    return messages
