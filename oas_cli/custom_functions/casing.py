from typing import Any, Dict, List
import re

def is_flat_case(input: str) -> bool:
    return bool(re.match(r'^[a-z]+$', input))

def is_camel_case(input: str) -> bool:
    return bool(re.match(r'^[a-z]+(?:[A-Z][a-z]+)*$', input))

def is_pascal_case(input: str) -> bool:
    return bool(re.match(r'^[A-Z][a-z]+(?:[A-Z][a-z]+)*$', input))

def is_kebab_case(input: str) -> bool:
    return bool(re.match(r'^[a-z]+(?:-[a-z]+)*$', input))

def is_cobol_case(input: str) -> bool:
    return bool(re.match(r'^[A-Z]+(?:-[A-Z]+)*$', input))

def is_snake_case(input: str) -> bool:
    return bool(re.match(r'^[a-z]+(?:_[a-z]+)*$', input))

def is_macro_case(input: str) -> bool:
    return bool(re.match(r'^[A-Z]+(?:_[A-Z]+)*$', input))

def casing(
    context: str, target_value: Any, function_options: Dict[str, str]
) -> List[str]:
    type = function_options.get('type')
    types = {
        'flat': is_flat_case(target_value),
        'camel': is_camel_case(target_value),
        'pascal': is_pascal_case(target_value),
        'kebab': is_kebab_case(target_value),
        'cobol': is_cobol_case(target_value),
        'snake': is_snake_case(target_value),
        'macro': is_macro_case(target_value),
    }
    if type not in types:
        return [f'Os tipos suportados são: {[type for type in types.keys()]}']
    else:
        if types.get(type) is False:
            return [f'{context} deve ser {type} case.']
    return []

    # disallow_digits = function_options.get('disallowDigits', False)
    # separator_char = function_options.get('separator.char')
    # separator_allow_leading	= function_options.get('separator.allowLeading', False)
    # return []