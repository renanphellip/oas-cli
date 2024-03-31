import pytest
from oas_cli.core_functions.casing import is_kebab_case


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('very-long-name', True),
        ('very-long-name-123', False),
        ('very-123-long-name', False),
        ('123-very-long-name', False),
        ('very-long name', False),
        ('very-long_name', False),
        ('__very-long-name', False),
        ('_very-long-name', False),
        ('_very-long_name', False),
        ('_very-long-name-123_very-long-name-123', False),
    ]
)
def test_is_kebab_case_with_disallow_digits_true(input, expected_result):
    assert is_kebab_case(input=input, disallow_digits=True, separator_char=None, separator_allow_leading=None) is expected_result


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('very-long-name', True),
        ('very-long-name-123', True),
        ('very-123-long-name', True),
        ('123-very-long-name', False),
        ('very-long name', False),
        ('very-long_name', False),
        ('__very-long-name', False),
        ('_very-long-name', False),
        ('_very-long_name', False),
        ('_very-long-name-123_very-long-name-123', False),
    ]
)
def test_is_kebab_case_with_disallow_digits_false(input, expected_result):
    assert is_kebab_case(input=input, disallow_digits=False, separator_char=None, separator_allow_leading=None) is expected_result


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('very-long-name', True),
        ('very-long-name-123', False),
        ('very-123-long-name', False),
        ('123-very-long-name', False),
        ('very-long name', False),
        ('very-long_name', True),
        ('__very-long-name', False),
        ('_very-long-name', False),
        ('_very-long_name', False),
        ('_very-long-name-123_very-long-name-123', False),
    ]
)
def test_is_kebab_case_with_disallow_digits_true_and_separator_char(input, expected_result):
    assert is_kebab_case(input=input, disallow_digits=True, separator_char='_', separator_allow_leading=None) is expected_result


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('very-long-name', True),
        ('very-long-name-123', True),
        ('very-123-long-name', True),
        ('123-very-long-name', False),
        ('very-long name', False),
        ('very-long_name', True),
        ('__very-long-name', False),
        ('_very-long-name', False),
        ('_very-long_name', False),
        ('_very-long-name-123_very-long-name-123', False),
    ]
)
def test_is_kebab_case_with_disallow_digits_false_and_separator_char(input, expected_result):
    assert is_kebab_case(input=input, disallow_digits=False, separator_char='_', separator_allow_leading=None) is expected_result


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('very-long-name', True),
        ('very-long-name-123', False),
        ('very-123-long-name', False),
        ('123-very-long-name', False),
        ('very-long name', False),
        ('very-long_name', True),
        ('__very-long-name', False),
        ('_very-long-name', True),
        ('_very-long_name', True),
        ('_very-long-name-123_very-long-name-123', False),
    ]
)
def test_is_kebab_case_with_disallow_digits_true_and_separator_char_and_separator_allow_leading_true(input, expected_result):
    assert is_kebab_case(input=input, disallow_digits=True, separator_char='_', separator_allow_leading=True) is expected_result


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('very-long-name', True),
        ('very-long-name-123', True),
        ('very-123-long-name', True),
        ('123-very-long-name', False),
        ('very-long name', False),
        ('very-long_name', True),
        ('__very-long-name', False),
        ('_very-long-name', True),
        ('_very-long_name', True),
        ('_very-long-name-123_very-long-name-123', True),
    ]
)
def test_is_kebab_case_with_disallow_digits_false_and_separator_char_and_separator_allow_leading_true(input, expected_result):
    assert is_kebab_case(input=input, disallow_digits=False, separator_char='_', separator_allow_leading=True) is expected_result
