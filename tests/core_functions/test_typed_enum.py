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
    assert errors[0] == f'The enum value {function_options['enum'][0]} must be of type {function_options['type']}.'
    assert errors[1] == f'The enum value {function_options['enum'][1]} must be of type {function_options['type']}.'
    assert errors[2] == f'{context} must be: {function_options['enum']}'


@pytest.mark.parametrize(
    'target_value, expected_error_count',
    [
        ('', 1),
        ('1', 0),
        ('2', 0),
        ('3', 0),
        (1, 2)
    ],
)
def test_typed_enum_with_type_string(target_value, expected_error_count):
    context = '$.myProperty'
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
    assert len(errors) == expected_error_count
    if expected_error_count == 2:
        assert errors[0] == f'The value {target_value} in {context} must be of type {function_options['type']}.'
        assert errors[1] == f'{context} must be: {function_options['enum']}'


@pytest.mark.parametrize(
    'target_value, expected_error_count',
    [
        (0, 1),
        (1, 0),
        (2, 0),
        (3, 0),
        ('1', 2)
    ],
)
def test_typed_enum_with_type_number(target_value, expected_error_count):
    context = '$.myProperty'
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
    assert len(errors) == expected_error_count
    if expected_error_count == 2:
        assert errors[0] == f'The value {target_value} in {context} must be of type {function_options['type']}.'
        assert errors[1] == f'{context} must be: {function_options['enum']}'
