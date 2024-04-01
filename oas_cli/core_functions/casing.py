from typing import Any, Dict, List
import re

def is_flat_case(input: str, disallow_digits: bool, separator_char: str, separator_allow_leading: bool) -> bool:
    regex = rf''
    if disallow_digits is True:
        regex = rf'[a-z]+'
        if separator_char:
            regex = rf'[a-z]+(?:{separator_char}[a-z]+)*'
            if separator_allow_leading is True:
                regex = rf'{separator_char}?[a-z]+(?:{separator_char}[a-z]+)*'
    else:
        regex = rf'[a-z]+[a-z0-9]*'
        if separator_char:
            regex = rf'[a-z]+[a-z0-9]*(?:{separator_char}[a-z]+[a-z0-9]*)*'
            if separator_allow_leading is True:
                regex = rf'{separator_char}?[a-z]+[a-z0-9]*(?:{separator_char}[a-z]+[a-z0-9]*)*'
    return bool(re.match(rf'^{regex}$', input))

def is_camel_case(input: str, disallow_digits: bool, separator_char: str, separator_allow_leading: bool) -> bool:
    regex = rf''
    if disallow_digits is True:
        regex = rf'[a-z]+(?:[A-Z][a-z]+)*'
        if separator_char:
            regex = rf'[a-z]+(?:[A-Z][a-z]+)*(?:{separator_char}?[a-z]+(?:[A-Z][a-z]+)*)*'
            if separator_allow_leading is True:
                regex = rf'{separator_char}?[a-z]+(?:[A-Z][a-z]+)*(?:{separator_char}?[a-z]+(?:[A-Z][a-z]+)*)*'
    else:
        regex = rf'[a-z]+(?:[A-Z][a-z]+|[A-Z][0-9]+|[0-9]*[A-Z][a-z]+)*'
        if separator_char:
            regex = rf'[a-z]+(?:[A-Z][a-z]+|[A-Z][0-9]+|[0-9]*[A-Z][a-z]+)*(?:{separator_char}?[a-z]+(?:[A-Z][a-z]+|[A-Z][0-9]+|[0-9]*[A-Z][a-z]+)*)*'
            if separator_allow_leading is True:
                regex = rf'{separator_char}?[a-z]+(?:[A-Z][a-z]+|[A-Z][0-9]+|[0-9]*[A-Z][a-z]+)*(?:{separator_char}?[a-z]+(?:[A-Z][a-z]+|[A-Z][0-9]+|[0-9]*[A-Z][a-z]+)*)*'
    return bool(re.match(rf'^{regex}$', input))

def is_pascal_case(input: str, disallow_digits: bool, separator_char: str, separator_allow_leading: bool) -> bool:
    regex = rf''
    if disallow_digits is True:
        regex = rf'[A-Z][a-z]+(?:[A-Z][a-z]+)*'
        if separator_char:
            regex = rf'[A-Z][a-z]+(?:[A-Z][a-z]+)*(?:{separator_char}?[A-Z][a-z]+(?:[A-Z][a-z]+)*)*'
            if separator_allow_leading is True:
                regex = rf'{separator_char}?[A-Z][a-z]+(?:[A-Z][a-z]+)*(?:{separator_char}?[A-Z][a-z]+(?:[A-Z][a-z]+)*)*'
    else:
        regex = rf'[A-Z][a-z]+(?:[A-Z][a-z]+|[A-Z][0-9]+|[0-9]*[A-Z][a-z]+)*'
        if separator_char:
            regex = rf'[A-Z][a-z]+(?:[A-Z][a-z]+|[A-Z][0-9]+|[0-9]*[A-Z][a-z]+)*(?:{separator_char}?[A-Z][a-z]+(?:[A-Z][a-z]+|[A-Z][0-9]+|[0-9]*[A-Z][a-z]+)*)*'
            if separator_allow_leading is True:
                regex = rf'{separator_char}?[A-Z][a-z]+(?:[A-Z][a-z]+|[A-Z][0-9]+|[0-9]*[A-Z][a-z]+)*(?:{separator_char}?[A-Z][a-z]+(?:[A-Z][a-z]+|[A-Z][0-9]+|[0-9]*[A-Z][a-z]+)*)*'
    return bool(re.match(rf'^{regex}$', input))

def is_kebab_case(input: str, disallow_digits: bool, separator_char: str, separator_allow_leading: bool) -> bool:
    regex = rf''
    if disallow_digits is True:
        regex = rf'[a-z]+(?:-[a-z]+)*'
        if separator_char:
            regex = rf'[a-z]+(?:-[a-z]+)*(?:{separator_char}?[a-z]+(?:-[a-z]+)*)*'
            if separator_allow_leading is True:
                regex = rf'{separator_char}?[a-z]+(?:-[a-z]+)*(?:{separator_char}?[a-z]+(?:-[a-z]+)*)*'
    else:
        regex = rf'[a-z]+(?:-[a-z0-9]+)*'
        if separator_char:
            regex = rf'[a-z]+(?:-[a-z0-9]+)*(?:{separator_char}?[a-z]+(?:-[a-z0-9]+)*)*'
            if separator_allow_leading is True:
                regex = rf'{separator_char}?[a-z]+(?:-[a-z0-9]+)*(?:{separator_char}?[a-z]+(?:-[a-z0-9]+)*)*'
    return bool(re.match(rf'^{regex}$', input))

def is_cobol_case(input: str, disallow_digits: bool, separator_char: str, separator_allow_leading: bool) -> bool:
    regex = rf''
    if disallow_digits is True:
        regex = rf'[A-Z]+(?:-[A-Z]+)*'
        if separator_char:
            regex = rf'[A-Z]+(?:-[A-Z]+)*(?:{separator_char}?[A-Z]+(?:-[A-Z]+)*)*'
            if separator_allow_leading is True:
                regex = rf'{separator_char}?[A-Z]+(?:-[A-Z]+)*(?:{separator_char}?[A-Z]+(?:-[A-Z]+)*)*'
    else:
        regex = rf'[A-Z]+(?:-[A-Z0-9]+)*'
        if separator_char:
            regex = rf'[A-Z]+(?:-[A-Z0-9]+)*(?:{separator_char}?[A-Z]+(?:-[A-Z0-9]+)*)*'
            if separator_allow_leading is True:
                regex = rf'{separator_char}?[A-Z]+(?:-[A-Z0-9]+)*(?:{separator_char}?[A-Z]+(?:-[A-Z0-9]+)*)*'
    return bool(re.match(rf'^{regex}$', input))

def is_snake_case(input: str, disallow_digits: bool, separator_char: str, separator_allow_leading: bool) -> bool:
    regex = rf''
    if disallow_digits is True:
        regex = rf'[a-z]+(?:_[a-z]+)*'
        if separator_char:
            regex = rf'[a-z]+(?:_[a-z]+)*(?:{separator_char}?[a-z]+(?:_[a-z]+)*)*'
            if separator_allow_leading is True:
                regex = rf'{separator_char}?[a-z]+(?:_[a-z]+)*(?:{separator_char}?[a-z]+(?:_[a-z]+)*)*'
    else:
        regex = rf'[a-z]+(?:_[a-z0-9]+)*'
        if separator_char:
            regex = rf'[a-z]+(?:_[a-z0-9]+)*(?:{separator_char}?[a-z]+(?:_[a-z0-9]+)*)*'
            if separator_allow_leading is True:
                regex = rf'{separator_char}?[a-z]+(?:_[a-z0-9]+)*(?:{separator_char}?[a-z]+(?:_[a-z0-9]+)*)*'
    return bool(re.match(rf'^{regex}$', input))

def is_macro_case(input: str, disallow_digits: bool, separator_char: str, separator_allow_leading: bool) -> bool:
    regex = rf''
    if disallow_digits is True:
        regex = rf'[A-Z]+(?:_[A-Z]+)*'
        if separator_char:
            regex = rf'[A-Z]+(?:_[A-Z]+)*(?:{separator_char}?[A-Z]+(?:_[A-Z]+)*)*'
            if separator_allow_leading is True:
                regex = rf'{separator_char}?[A-Z]+(?:_[A-Z]+)*(?:{separator_char}?[A-Z]+(?:_[A-Z]+)*)*'
    else:
        regex = rf'[A-Z]+(?:_[A-Z0-9]+)*'
        if separator_char:
            regex = rf'[A-Z]+(?:_[A-Z0-9]+)*(?:{separator_char}?[A-Z]+(?:_[A-Z0-9]+)*)*'
            if separator_allow_leading is True:
                regex = rf'{separator_char}?[A-Z]+(?:_[A-Z0-9]+)*(?:{separator_char}?[A-Z]+(?:_[A-Z0-9]+)*)*'
    return bool(re.match(rf'^{regex}$', input))

def casing(
    context: str, target_value: Any, function_options: Dict[str, str]
) -> List[str]:
    disallow_digits = function_options.get('disallowDigits')
    separator_char = function_options.get('separator.char')
    separator_allow_leading = function_options.get('separator.allowLeading')
    type = function_options.get('type')
    types = {
        'flat': is_flat_case(target_value, disallow_digits, separator_char, separator_allow_leading),
        'camel': is_camel_case(target_value, disallow_digits, separator_char, separator_allow_leading),
        'pascal': is_pascal_case(target_value, disallow_digits, separator_char, separator_allow_leading),
        'kebab': is_kebab_case(target_value, disallow_digits, separator_char, separator_allow_leading),
        'cobol': is_cobol_case(target_value, disallow_digits, separator_char, separator_allow_leading),
        'snake': is_snake_case(target_value, disallow_digits, separator_char, separator_allow_leading),
        'macro': is_macro_case(target_value, disallow_digits, separator_char, separator_allow_leading),
    }
    if types.get(type) is False:
        return [f'{context} must be {type} case.']
    return []