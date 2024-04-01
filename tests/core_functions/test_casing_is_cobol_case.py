import pytest

from oas_cli.core_functions.casing import is_cobol_case


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('VERY-LONG-NAME', True),
        ('VERY-LONG-NAME-123', False),
        ('VERY-123-LONG-NAME', False),
        ('123-VERY-LONG-NAME', False),
        ('VERY-LONG NAME', False),
        ('VERY-LONG_NAME', False),
        ('__VERY-LONG-NAME', False),
        ('_VERY-LONG-NAME', False),
        ('_VERY-LONG_NAME', False),
        ('_VERY-LONG-NAME-123_VERY-LONG-NAME-123', False),
    ],
)
def test_is_cobol_case_with_disallow_digits_true(input, expected_result):
    assert (
        is_cobol_case(
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
        ('VERY-LONG-NAME', True),
        ('VERY-LONG-NAME-123', True),
        ('VERY-123-LONG-NAME', True),
        ('123-VERY-LONG-NAME', False),
        ('VERY-LONG NAME', False),
        ('VERY-LONG_NAME', False),
        ('__VERY-LONG-NAME', False),
        ('_VERY-LONG-NAME', False),
        ('_VERY-LONG_NAME', False),
        ('_VERY-LONG-NAME-123_VERY-LONG-NAME-123', False),
    ],
)
def test_is_cobol_case_with_disallow_digits_false(input, expected_result):
    assert (
        is_cobol_case(
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
        ('VERY-LONG-NAME', True),
        ('VERY-LONG-NAME-123', False),
        ('VERY-123-LONG-NAME', False),
        ('123-VERY-LONG-NAME', False),
        ('VERY-LONG NAME', False),
        ('VERY-LONG_NAME', True),
        ('__VERY-LONG-NAME', False),
        ('_VERY-LONG-NAME', False),
        ('_VERY-LONG_NAME', False),
        ('_VERY-LONG-NAME-123_VERY-LONG-NAME-123', False),
    ],
)
def test_is_cobol_case_with_disallow_digits_true_and_separator_char(
    input, expected_result
):
    assert (
        is_cobol_case(
            input=input,
            disallow_digits=True,
            separator_char='_',
            separator_allow_leading=None,
        )
        is expected_result
    )


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('VERY-LONG-NAME', True),
        ('VERY-LONG-NAME-123', True),
        ('VERY-123-LONG-NAME', True),
        ('123-VERY-LONG-NAME', False),
        ('VERY-LONG NAME', False),
        ('VERY-LONG_NAME', True),
        ('__VERY-LONG-NAME', False),
        ('_VERY-LONG-NAME', False),
        ('_VERY-LONG_NAME', False),
        ('_VERY-LONG-NAME-123_VERY-LONG-NAME-123', False),
    ],
)
def test_is_cobol_case_with_disallow_digits_false_and_separator_char(
    input, expected_result
):
    assert (
        is_cobol_case(
            input=input,
            disallow_digits=False,
            separator_char='_',
            separator_allow_leading=None,
        )
        is expected_result
    )


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('VERY-LONG-NAME', True),
        ('VERY-LONG-NAME-123', False),
        ('VERY-123-LONG-NAME', False),
        ('123-VERY-LONG-NAME', False),
        ('VERY-LONG NAME', False),
        ('VERY-LONG_NAME', True),
        ('__VERY-LONG-NAME', False),
        ('_VERY-LONG-NAME', True),
        ('_VERY-LONG_NAME', True),
        ('_VERY-LONG-NAME-123_VERY-LONG-NAME-123', False),
    ],
)
def test_is_cobol_case_with_disallow_digits_true_and_separator_char_and_separator_allow_leading_true(
    input, expected_result
):
    assert (
        is_cobol_case(
            input=input,
            disallow_digits=True,
            separator_char='_',
            separator_allow_leading=True,
        )
        is expected_result
    )


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('VERY-LONG-NAME', True),
        ('VERY-LONG-NAME-123', True),
        ('VERY-123-LONG-NAME', True),
        ('123-VERY-LONG-NAME', False),
        ('VERY-LONG NAME', False),
        ('VERY-LONG_NAME', True),
        ('__VERY-LONG-NAME', False),
        ('_VERY-LONG-NAME', True),
        ('_VERY-LONG_NAME', True),
        ('_VERY-LONG-NAME-123_VERY-LONG-NAME-123', True),
    ],
)
def test_is_cobol_case_with_disallow_digits_false_and_separator_char_and_separator_allow_leading_true(
    input, expected_result
):
    assert (
        is_cobol_case(
            input=input,
            disallow_digits=False,
            separator_char='_',
            separator_allow_leading=True,
        )
        is expected_result
    )
