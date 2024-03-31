import pytest
from oas_cli.core_functions.casing import is_snake_case


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('very_long_name', True),
        ('very_long_name_123', False),
        ('very_123_long_name', False),
        ('123_very_long_name', False),
        ('very_long name', False),
        ('very_long-name', False),
        ('--very_long_name', False),
        ('-very_long_name', False),
        ('-very_long-name', False),
        ('-very_long_name_123-very_long_name_123', False),
    ]
)
def test_is_snake_case_with_disallow_digits_true(input, expected_result):
    assert is_snake_case(input=input, disallow_digits=True, separator_char=None, separator_allow_leading=None) is expected_result


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('very_long_name', True),
        ('very_long_name_123', True),
        ('very_123_long_name', True),
        ('123_very_long_name', False),
        ('very_long name', False),
        ('very_long-name', False),
        ('--very_long_name', False),
        ('-very_long_name', False),
        ('-very_long-name', False),
        ('-very_long_name_123-very_long_name_123', False),
    ]
)
def test_is_snake_case_with_disallow_digits_false(input, expected_result):
    assert is_snake_case(input=input, disallow_digits=False, separator_char=None, separator_allow_leading=None) is expected_result


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('very_long_name', True),
        ('very_long_name_123', False),
        ('very_123_long_name', False),
        ('123_very_long_name', False),
        ('very_long name', False),
        ('very_long-name', True),
        ('--very_long_name', False),
        ('-very_long_name', False),
        ('-very_long-name', False),
        ('-very_long_name_123-very_long_name_123', False),
    ]
)
def test_is_snake_case_with_disallow_digits_true_and_separator_char(input, expected_result):
    assert is_snake_case(input=input, disallow_digits=True, separator_char='-', separator_allow_leading=None) is expected_result


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('very_long_name', True),
        ('very_long_name_123', True),
        ('very_123_long_name', True),
        ('123_very_long_name', False),
        ('very_long name', False),
        ('very_long-name', True),
        ('--very_long_name', False),
        ('-very_long_name', False),
        ('-very_long-name', False),
        ('-very_long_name_123-very_long_name_123', False),
    ]
)
def test_is_snake_case_with_disallow_digits_false_and_separator_char(input, expected_result):
    assert is_snake_case(input=input, disallow_digits=False, separator_char='-', separator_allow_leading=None) is expected_result


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('very_long_name', True),
        ('very_long_name_123', False),
        ('very_123_long_name', False),
        ('123_very_long_name', False),
        ('very_long name', False),
        ('very_long-name', True),
        ('--very_long_name', False),
        ('-very_long_name', True),
        ('-very_long-name', True),
        ('-very_long_name_123-very_long_name_123', False),
    ]
)
def test_is_snake_case_with_disallow_digits_true_and_separator_char_and_separator_allow_leading_true(input, expected_result):
    assert is_snake_case(input=input, disallow_digits=True, separator_char='-', separator_allow_leading=True) is expected_result


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('very_long_name', True),
        ('very_long_name_123', True),
        ('very_123_long_name', True),
        ('123_very_long_name', False),
        ('very_long name', False),
        ('very_long-name', True),
        ('--very_long_name', False),
        ('-very_long_name', True),
        ('-very_long-name', True),
        ('-very_long_name_123-very_long_name_123', True),
    ]
)
def test_is_snake_case_with_disallow_digits_false_and_separator_char_and_separator_allow_leading_true(input, expected_result):
    assert is_snake_case(input=input, disallow_digits=False, separator_char='-', separator_allow_leading=True) is expected_result
