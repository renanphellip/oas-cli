import pytest
from oas_cli.core_functions.casing import is_flat_case


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('verylongname', True),
        ('verylongname123', False),
        ('very123longname', False),
        ('123verylongname', False),
        ('verylong name', False),
        ('verylong-name', False),
        ('--verylongname', False),
        ('-verylongname', False),
        ('-verylong-name', False),
        ('-verylongname123-verylongname123', False),
    ]
)
def test_is_flat_case_with_disallow_digits_true(input, expected_result):
    assert is_flat_case(input=input, disallow_digits=True, separator_char=None, separator_allow_leading=None) is expected_result


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('verylongname', True),
        ('verylongname123', True),
        ('very123longname', True),
        ('123verylongname', False),
        ('verylong name', False),
        ('verylong-name', False),
        ('--verylongname', False),
        ('-verylongname', False),
        ('-verylong-name', False),
        ('-verylongname123-verylongname123', False),
    ]
)
def test_is_flat_case_with_disallow_digits_false(input, expected_result):
    assert is_flat_case(input=input, disallow_digits=False, separator_char=None, separator_allow_leading=None) is expected_result


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('verylongname', True),
        ('verylongname123', False),
        ('very123longname', False),
        ('123verylongname', False),
        ('verylong name', False),
        ('verylong-name', True),
        ('--verylongname', False),
        ('-verylongname', False),
        ('-verylong-name', False),
        ('-verylongname123-verylongname123', False),
    ]
)
def test_is_flat_case_with_disallow_digits_true_and_separator_char(input, expected_result):
    assert is_flat_case(input=input, disallow_digits=True, separator_char='-', separator_allow_leading=None) is expected_result


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('verylongname', True),
        ('verylongname123', True),
        ('very123longname', True),
        ('123verylongname', False),
        ('verylong name', False),
        ('verylong-name', True),
        ('--verylongname', False),
        ('-verylongname', False),
        ('-verylong-name', False),
        ('-verylongname123-verylongname123', False),
    ]
)
def test_is_flat_case_with_disallow_digits_false_and_separator_char(input, expected_result):
    assert is_flat_case(input=input, disallow_digits=False, separator_char='-', separator_allow_leading=None) is expected_result


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('verylongname', True),
        ('verylongname123', False),
        ('very123longname', False),
        ('123verylongname', False),
        ('verylong name', False),
        ('verylong-name', True),
        ('--verylongname', False),
        ('-verylongname', True),
        ('-verylong-name', True),
        ('-verylongname123-verylongname123', False),
    ]
)
def test_is_flat_case_with_disallow_digits_true_and_separator_char_and_separator_allow_leading_true(input, expected_result):
    assert is_flat_case(input=input, disallow_digits=True, separator_char='-', separator_allow_leading=True) is expected_result


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('verylongname', True),
        ('verylongname123', True),
        ('very123longname', True),
        ('123verylongname', False),
        ('verylong name', False),
        ('verylong-name', True),
        ('--verylongname', False),
        ('-verylongname', True),
        ('-verylong-name', True),
        ('-verylongname123-verylongname123', True),
    ]
)
def test_is_flat_case_with_disallow_digits_false_and_separator_char_and_separator_allow_leading_true(input, expected_result):
    assert is_flat_case(input=input, disallow_digits=False, separator_char='-', separator_allow_leading=True) is expected_result
