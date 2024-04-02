import pytest
from oas_cli.core_functions.length import length


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        ('ab', 0),
        ('abcde', 0),
        ('abcdefghij', 0),
        ('a', 1),
        ('abcdefghijk', 1),
    ],
)
def test_length_with_strings(input, expected_errors):
    context = '$'
    target_value = {
        'myProperty': input
    }
    function_options = {
        'min': 2,
        'max': 10
    }
    field_name = 'myProperty'
    errors = length(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=field_name,
    )
    assert len(errors) == expected_errors


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        (2, 0),
        (5, 0),
        (10, 0),
        (1, 1),
        (11, 1),
    ],
)
def test_length_with_numbers(input, expected_errors):
    context = '$'
    target_value = {
        'myProperty': input
    }
    function_options = {
        'min': 2,
        'max': 10
    }
    field_name = 'myProperty'
    errors = length(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=field_name,
    )
    assert len(errors) == expected_errors


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        ([1, 2], 0),
        ([1, 2, 3, 4, 5], 0),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0),
        ([1], 1),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 1),
    ],
)
def test_length_with_lists(input, expected_errors):
    context = '$'
    target_value = {
        'myProperty': input
    }
    function_options = {
        'min': 2,
        'max': 10
    }
    field_name = 'myProperty'
    errors = length(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=field_name,
    )
    assert len(errors) == expected_errors


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        (
            {
                'a': 1,
                'b': 2
            },
            0
        ),
        (
            {
                'a': 1,
                'b': 2,
                'c': 3,
                'd': 4,
                'e': 5
            },
            0
        ),
        (
            {
                'a': 1,
                'b': 2,
                'c': 3,
                'd': 4,
                'e': 5,
                'f': 6,
                'g': 7,
                'h': 8,
                'i': 9,
                'j': 10
            },
            0
        ),
        (
            {
                'a':'1'
            },
            1
        ),
        (
            {
                'a': 1,
                'b': 2,
                'c': 3,
                'd': 4,
                'e': 5,
                'f': 6,
                'g': 7,
                'h': 8,
                'i': 9,
                'j': 10,
                'k': 11
            },
            1
        ),
    ],
)
def test_length_with_dicts(input, expected_errors):
    context = '$'
    target_value = {
        'myProperty': input
    }
    function_options = {
        'min': 2,
        'max': 10
    }
    field_name = 'myProperty'
    errors = length(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=field_name,
    )
    assert len(errors) == expected_errors
