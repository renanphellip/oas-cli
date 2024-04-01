import pytest

from oas_cli.core_functions.casing import is_macro_case


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('VERY_LONG_NAME', True),
        ('VERY_LONG_NAME_123', False),
        ('VERY_123_LONG_NAME', False),
        ('123_VERY_LONG_NAME', False),
        ('VERY_LONG NAME', False),
        ('VERY_LONG-NAME', False),
        ('--VERY_LONG_NAME', False),
        ('-VERY_LONG_NAME', False),
        ('-VERY_LONG-NAME', False),
        ('-VERY_LONG_NAME_123-VERY_LONG_NAME_123', False),
    ],
)
def test_is_macro_case_with_disallow_digits_true(input, expected_result):
    assert (
        is_macro_case(
            input=input,
            disallow_digits=True,
            separator_char=None,
            separator_allow_leading=None,
        )
        is expected_result
    )


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('VERY_LONG_NAME', True),
        ('VERY_LONG_NAME_123', True),
        ('VERY_123_LONG_NAME', True),
        ('123_VERY_LONG_NAME', False),
        ('VERY_LONG NAME', False),
        ('VERY_LONG-NAME', False),
        ('--VERY_LONG_NAME', False),
        ('-VERY_LONG_NAME', False),
        ('-VERY_LONG-NAME', False),
        ('-VERY_LONG_NAME_123-VERY_LONG_NAME_123', False),
    ],
)
def test_is_macro_case_with_disallow_digits_false(input, expected_result):
    assert (
        is_macro_case(
            input=input,
            disallow_digits=False,
            separator_char=None,
            separator_allow_leading=None,
        )
        is expected_result
    )


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('VERY_LONG_NAME', True),
        ('VERY_LONG_NAME_123', False),
        ('VERY_123_LONG_NAME', False),
        ('123_VERY_LONG_NAME', False),
        ('VERY_LONG NAME', False),
        ('VERY_LONG-NAME', True),
        ('--VERY_LONG_NAME', False),
        ('-VERY_LONG_NAME', False),
        ('-VERY_LONG-NAME', False),
        ('-VERY_LONG_NAME_123-VERY_LONG_NAME_123', False),
    ],
)
def test_is_macro_case_with_disallow_digits_true_and_separator_char(
    input, expected_result
):
    assert (
        is_macro_case(
            input=input,
            disallow_digits=True,
            separator_char='-',
            separator_allow_leading=None,
        )
        is expected_result
    )


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('VERY_LONG_NAME', True),
        ('VERY_LONG_NAME_123', True),
        ('VERY_123_LONG_NAME', True),
        ('123_VERY_LONG_NAME', False),
        ('VERY_LONG NAME', False),
        ('VERY_LONG-NAME', True),
        ('--VERY_LONG_NAME', False),
        ('-VERY_LONG_NAME', False),
        ('-VERY_LONG-NAME', False),
        ('-VERY_LONG_NAME_123-VERY_LONG_NAME_123', False),
    ],
)
def test_is_macro_case_with_disallow_digits_false_and_separator_char(
    input, expected_result
):
    assert (
        is_macro_case(
            input=input,
            disallow_digits=False,
            separator_char='-',
            separator_allow_leading=None,
        )
        is expected_result
    )


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('VERY_LONG_NAME', True),
        ('VERY_LONG_NAME_123', False),
        ('VERY_123_LONG_NAME', False),
        ('123_VERY_LONG_NAME', False),
        ('VERY_LONG NAME', False),
        ('VERY_LONG-NAME', True),
        ('--VERY_LONG_NAME', False),
        ('-VERY_LONG_NAME', True),
        ('-VERY_LONG-NAME', True),
        ('-VERY_LONG_NAME_123-VERY_LONG_NAME_123', False),
    ],
)
def test_is_macro_case_with_disallow_digits_true_and_separator_char_and_separator_allow_leading_true(
    input, expected_result
):
    assert (
        is_macro_case(
            input=input,
            disallow_digits=True,
            separator_char='-',
            separator_allow_leading=True,
        )
        is expected_result
    )


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('VERY_LONG_NAME', True),
        ('VERY_LONG_NAME_123', True),
        ('VERY_123_LONG_NAME', True),
        ('123_VERY_LONG_NAME', False),
        ('VERY_LONG NAME', False),
        ('VERY_LONG-NAME', True),
        ('--VERY_LONG_NAME', False),
        ('-VERY_LONG_NAME', True),
        ('-VERY_LONG-NAME', True),
        ('-VERY_LONG_NAME_123-VERY_LONG_NAME_123', True),
    ],
)
def test_is_macro_case_with_disallow_digits_false_and_separator_char_and_separator_allow_leading_true(
    input, expected_result
):
    assert (
        is_macro_case(
            input=input,
            disallow_digits=False,
            separator_char='-',
            separator_allow_leading=True,
        )
        is expected_result
    )
