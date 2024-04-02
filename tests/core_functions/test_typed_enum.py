import pytest
from oas_cli.core_functions.typed_enum import typedEnum


def test_typed_enum_with_invalid_enum_values_with_type():
    context = '$.myProperty'
    target_value = 1
    function_options = {
        'enum': [
            '1',
            '2',
        ],
        'type': 'number'
    }
    errors = typedEnum(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=None,
    )
    assert len(errors) == 3
    assert errors[0] == f'The enum value {function_options.get('enum')[0]} must be of type {function_options.get('type')}.'
    assert errors[1] == f'The enum value {function_options.get('enum')[1]} must be of type {function_options.get('type')}.'
    assert errors[2] == f'{context} must be: {function_options.get('enum')}'


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        ('', 1),
        ('1', 0),
        ('2', 0),
        ('3', 0),
        (1, 2)
    ],
)
def test_typed_enum_with_type_string(input, expected_errors):
    context = '$.myProperty'
    target_value = input
    function_options = {
        'enum': [
            '1',
            '2',
            '3',
        ],
        'type': 'string'
    }
    errors = typedEnum(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=None,
    )
    assert len(errors) == expected_errors
    if expected_errors == 2:
        assert errors[0] == f'The value {target_value} in {context} must be of type {function_options.get('type')}.'
        assert errors[1] == f'{context} must be: {function_options.get('enum')}'


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        (0, 1),
        (1, 0),
        (2, 0),
        (3, 0),
        ('1', 2)
    ],
)
def test_typed_enum_with_type_number(input, expected_errors):
    context = '$.myProperty'
    target_value = input
    function_options = {
        'enum': [
            1,
            2,
            3,
        ],
        'type': 'number'
    }
    errors = typedEnum(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=None,
    )
    assert len(errors) == expected_errors
    if expected_errors == 2:
        assert errors[0] == f'The value {target_value} in {context} must be of type {function_options.get('type')}.'
        assert errors[1] == f'{context} must be: {function_options.get('enum')}'