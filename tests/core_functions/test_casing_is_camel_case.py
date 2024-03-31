import pytest
from oas_cli.core_functions.casing import is_camel_case


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('veryLongName', True),
        ('VeryLongName', False),
        ('123veryLongName', False),
        ('123VeryLongName', False),
        ('veryLongNameV123', False),
        ('veryLongName123V', False),
        ('veryLongName123Version', False),
        ('veryLongName-veryLongName', False),
        ('veryLongName-VeryLongName', False),
        ('veryLongNameV123-veryLongNameV123', False),
        ('veryLongName123V-veryLongName123V', False),
        ('veryLongName123Version-veryLongName123Version', False),
        ('-veryLongName', False),
        ('-veryLongName-veryLongName', False),
        ('--veryLongName-veryLongName', False),
        ('-veryLongName-VeryLongName', False),
        ('-veryLongNameV123-veryLongNameV123', False),
        ('-veryLongName123V-veryLongName123V', False),
        ('-veryLongName123Version-veryLongName123Version', False),
    ]
)
def test_is_camel_case_with_disallow_digits_true(input, expected_result):
    assert is_camel_case(input=input, disallow_digits=True, separator_char=None, separator_allow_leading=None) is expected_result


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('veryLongName', True),
        ('VeryLongName', False),
        ('123veryLongName', False),
        ('123VeryLongName', False),
        ('veryLongNameV123', True),
        ('veryLongName123V', False),
        ('veryLongName123Version', True),
        ('veryLongName-veryLongName', False),
        ('veryLongName-VeryLongName', False),
        ('veryLongNameV123-veryLongNameV123', False),
        ('veryLongName123V-veryLongName123V', False),
        ('veryLongName123Version-veryLongName123Version', False),
        ('-veryLongName', False),
        ('-veryLongName-veryLongName', False),
        ('--veryLongName-veryLongName', False),
        ('-veryLongName-VeryLongName', False),
        ('-veryLongNameV123-veryLongNameV123', False),
        ('-veryLongName123V-veryLongName123V', False),
        ('-veryLongName123Version-veryLongName123Version', False),
    ]
)
def test_is_camel_case_with_disallow_digits_false(input, expected_result):
    assert is_camel_case(input=input, disallow_digits=False, separator_char=None, separator_allow_leading=None) is expected_result


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('veryLongName', True),
        ('VeryLongName', False),
        ('123veryLongName', False),
        ('123VeryLongName', False),
        ('veryLongNameV123', False),
        ('veryLongName123V', False),
        ('veryLongName123Version', False),
        ('veryLongName-veryLongName', True),
        ('veryLongName-VeryLongName', False),
        ('veryLongNameV123-veryLongNameV123', False),
        ('veryLongName123V-veryLongName123V', False),
        ('veryLongName123Version-veryLongName123Version', False),
        ('-veryLongName', False),
        ('-veryLongName-veryLongName', False),
        ('--veryLongName-veryLongName', False),
        ('-veryLongName-VeryLongName', False),
        ('-veryLongNameV123-veryLongNameV123', False),
        ('-veryLongName123V-veryLongName123V', False),
        ('-veryLongName123Version-veryLongName123Version', False),
    ]
)
def test_is_camel_case_with_disallow_digits_true_and_separator_char(input, expected_result):
    assert is_camel_case(input=input, disallow_digits=True, separator_char='-', separator_allow_leading=None) is expected_result


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('veryLongName', True),
        ('VeryLongName', False),
        ('123veryLongName', False),
        ('123VeryLongName', False),
        ('veryLongNameV123', True),
        ('veryLongName123V', False),
        ('veryLongName123Version', True),
        ('veryLongName-veryLongName', True),
        ('veryLongName-VeryLongName', False),
        ('veryLongNameV123-veryLongNameV123', True),
        ('veryLongName123V-veryLongName123V', False),
        ('veryLongName123Version-veryLongName123Version', True),
        ('-veryLongName', False),
        ('-veryLongName-veryLongName', False),
        ('--veryLongName-veryLongName', False),
        ('-veryLongName-VeryLongName', False),
        ('-veryLongNameV123-veryLongNameV123', False),
        ('-veryLongName123V-veryLongName123V', False),
        ('-veryLongName123Version-veryLongName123Version', False),
    ]
)
def test_is_camel_case_with_disallow_digits_false_and_separator_char(input, expected_result):
    assert is_camel_case(input=input, disallow_digits=False, separator_char='-', separator_allow_leading=None) is expected_result


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('veryLongName', True),
        ('VeryLongName', False),
        ('123veryLongName', False),
        ('123VeryLongName', False),
        ('veryLongNameV123', False),
        ('veryLongName123V', False),
        ('veryLongName123Version', False),
        ('veryLongName-veryLongName', True),
        ('veryLongName-VeryLongName', False),
        ('veryLongNameV123-veryLongNameV123', False),
        ('veryLongName123V-veryLongName123V', False),
        ('veryLongName123Version-veryLongName123Version', False),
        ('-veryLongName', True),
        ('-veryLongName-veryLongName', True),
        ('--veryLongName-veryLongName', False),
        ('-veryLongName-VeryLongName', False),
        ('-veryLongNameV123-veryLongNameV123', False),
        ('-veryLongName123V-veryLongName123V', False),
        ('-veryLongName123Version-veryLongName123Version', False),
    ]
)
def test_is_camel_case_with_disallow_digits_true_and_separator_char_and_separator_allow_leading_true(input, expected_result):
    assert is_camel_case(input=input, disallow_digits=True, separator_char='-', separator_allow_leading=True) is expected_result


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('veryLongName', True),
        ('VeryLongName', False),
        ('123veryLongName', False),
        ('123VeryLongName', False),
        ('veryLongNameV123', True),
        ('veryLongName123V', False),
        ('veryLongName123Version', True),
        ('veryLongName-veryLongName', True),
        ('veryLongName-VeryLongName', False),
        ('veryLongNameV123-veryLongNameV123', True),
        ('veryLongName123V-veryLongName123V', False),
        ('veryLongName123Version-veryLongName123Version', True),
        ('-veryLongName', True),
        ('-veryLongName-veryLongName', True),
        ('--veryLongName-veryLongName', False),
        ('-veryLongName-VeryLongName', False),
        ('-veryLongNameV123-veryLongNameV123', True),
        ('-veryLongName123V-veryLongName123V', False),
        ('-veryLongName123Version-veryLongName123Version', True),
    ]
)
def test_is_camel_case_with_disallow_digits_false_and_separator_char_and_separator_allow_leading_true(input, expected_result):
    assert is_camel_case(input=input, disallow_digits=False, separator_char='-', separator_allow_leading=True) is expected_result
