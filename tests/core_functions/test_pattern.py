import pytest
from oas_cli.core_functions.pattern import pattern


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        ('', 0),
        ('TESTING', 0),
        ('123', 1),
        ('123TESTING', 1),
        ('TESTING123', 1),
        ('123TESTING123', 1),
    ],
)
def test_pattern_with_match(input, expected_errors):
    context = '$'
    target_value = input
    function_options = {
        'match': '^[A-Z]*$'
    }
    errors = pattern(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=None,
    )
    assert len(errors) == expected_errors



@pytest.mark.parametrize(
    'input, expected_errors',
    [
        ('', 1),
        ('TESTING', 1),
        ('123', 0),
        ('123TESTING', 0),
        ('TESTING123', 0),
        ('123TESTING123', 0),
    ],
)
def test_pattern_with_not_match(input, expected_errors):
    context = '$'
    target_value = input
    function_options = {
        'notMatch': '^[A-Z]*$'
    }
    errors = pattern(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=None,
    )
    assert len(errors) == expected_errors


def test_pattern_with_match_and_not_match():
    context = '$'
    target_value = ''
    function_options = {
        'match': '^[0-9]+$',
        'notMatch': '^[A-Z]*$'
    }
    errors = pattern(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=None,
    )
    assert len(errors) == 2
    assert errors[0] == '$ must match this regex: ^[0-9]+$'
    assert errors[1] == '$ must not match this regex: ^[A-Z]*$'