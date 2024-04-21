import pytest

from oas_cli.core_functions.pattern import pattern


@pytest.mark.parametrize(
    'target_value, expected_error_count',
    [
        ('', 0),
        ('TESTING', 0),
        ('123', 1),
        ('123TESTING', 1),
        ('TESTING123', 1),
        ('123TESTING123', 1),
    ],
)
def test_pattern_with_match(target_value, expected_error_count):
    context = '$'
    function_options = {
        'match': '^[A-Z]*$'
    }
    errors = pattern(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=None,
    )
    assert len(errors) == expected_error_count
    if len(errors) == 1:
        assert errors[0] == f'{context} must match this regex: {function_options['match']}'


@pytest.mark.parametrize(
    'target_value, expected_error_count',
    [
        ('', 1),
        ('TESTING', 1),
        ('123', 0),
        ('123TESTING', 0),
        ('TESTING123', 0),
        ('123TESTING123', 0),
    ],
)
def test_pattern_with_not_match(target_value, expected_error_count):
    context = '$'
    function_options = {
        'notMatch': '^[A-Z]*$'
    }
    errors = pattern(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=None,
    )
    assert len(errors) == expected_error_count
    if len(errors) == 1:
        assert errors[0] == f'{context} must not match this regex: {function_options['notMatch']}'


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
    assert errors[0] == f'{context} must match this regex: {function_options['match']}'
    assert errors[1] == f'{context} must not match this regex: {function_options['notMatch']}'
