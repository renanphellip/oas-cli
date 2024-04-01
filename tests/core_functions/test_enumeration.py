import pytest
from oas_cli.core_functions.enumeration import enumeration


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        ('1', 0),
        ('2', 0),
        ('3', 0),
        ('0', 1),
        ('', 1),
        (1, 1),
    ],
)
def test_enumeration_with_strings(input, expected_errors):
    context = '$'
    target_value = {
        'myProperty': input
    }
    function_options = {
        'values': [
            '1',
            '2',
            '3'
        ]
    }
    field_name = 'myProperty'
    errors = enumeration(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=field_name,
    )
    assert len(errors) == expected_errors


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        (123, 0),
        (456, 0),
        (789, 0),
        (0, 1),
        ('123', 1),
    ],
)
def test_enumeration_with_numbers(input, expected_errors):
    context = '$'
    target_value = {
        'myProperty': input
    }
    function_options = {
        'values': [
            123,
            456,
            789
        ]
    }
    field_name = 'myProperty'
    errors = enumeration(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=field_name,
    )
    assert len(errors) == expected_errors


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        ('123', 0),
        (456, 0),
        (True, 0),
        (123, 1),
        ('456', 1),
        ('True', 1),
        (None, 1),
    ],
)
def test_enumeration_with_any_type(input, expected_errors):
    context = '$'
    target_value = {
        'myProperty': input
    }
    function_options = {
        'values': [
            '123',
            456,
            True
        ]
    }
    field_name = 'myProperty'
    errors = enumeration(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=field_name,
    )
    assert len(errors) == expected_errors
