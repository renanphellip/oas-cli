import pytest

from oas_cli.core_functions.casing import is_pascal_case


@pytest.mark.parametrize(
    'input, expected_result',
    [
        ('VeryLongName', True),
        ('veryLongName', False),
        ('123veryLongName', False),
        ('123VeryLongName', False),
        ('VeryLongNameV123', False),
        ('VeryLongName123V', False),
        ('VeryLongName123Version', False),
        ('VeryLongName-veryLongName', False),
        ('VeryLongName-VeryLongName', False),
        ('VeryLongNameV123-VeryLongNameV123', False),
        ('VeryLongName123V-VeryLongName123V', False),
        ('VeryLongName123Version-VeryLongName123Version', False),
        ('-VeryLongName', False),
        ('-VeryLongName-VeryLongName', False),
        ('--VeryLongName-VeryLongName', False),
        ('-VeryLongName-veryLongName', False),
        ('-VeryLongNameV123-VeryLongNameV123', False),
        ('-VeryLongName123V-VeryLongName123V', False),
        ('-VeryLongName123Version-VeryLongName123Version', False),
    ],
)
def test_is_pascal_case_with_disallow_digits_true(input, expected_result):
    assert (
        is_pascal_case(
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
        ('VeryLongName', True),
        ('veryLongName', False),
        ('123veryLongName', False),
        ('123VeryLongName', False),
        ('VeryLongNameV123', True),
        ('VeryLongName123V', False),
        ('VeryLongName123Version', True),
        ('VeryLongName-veryLongName', False),
        ('VeryLongName-VeryLongName', False),
        ('VeryLongNameV123-VeryLongNameV123', False),
        ('VeryLongName123V-VeryLongName123V', False),
        ('VeryLongName123Version-VeryLongName123Version', False),
        ('-VeryLongName', False),
        ('-VeryLongName-VeryLongName', False),
        ('--VeryLongName-VeryLongName', False),
        ('-VeryLongName-veryLongName', False),
        ('-VeryLongNameV123-VeryLongNameV123', False),
        ('-VeryLongName123V-VeryLongName123V', False),
        ('-VeryLongName123Version-VeryLongName123Version', False),
    ],
)
def test_is_pascal_case_with_disallow_digits_false(input, expected_result):
    assert (
        is_pascal_case(
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
        ('VeryLongName', True),
        ('veryLongName', False),
        ('123veryLongName', False),
        ('123VeryLongName', False),
        ('VeryLongNameV123', False),
        ('VeryLongName123V', False),
        ('VeryLongName123Version', False),
        ('VeryLongName-veryLongName', False),
        ('VeryLongName-VeryLongName', True),
        ('VeryLongNameV123-VeryLongNameV123', False),
        ('VeryLongName123V-VeryLongName123V', False),
        ('VeryLongName123Version-VeryLongName123Version', False),
        ('-VeryLongName', False),
        ('-VeryLongName-VeryLongName', False),
        ('--VeryLongName-VeryLongName', False),
        ('-VeryLongName-veryLongName', False),
        ('-VeryLongNameV123-VeryLongNameV123', False),
        ('-VeryLongName123V-VeryLongName123V', False),
        ('-VeryLongName123Version-VeryLongName123Version', False),
    ],
)
def test_is_pascal_case_with_disallow_digits_true_and_separator_char(
    input, expected_result
):
    assert (
        is_pascal_case(
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
        ('VeryLongName', True),
        ('veryLongName', False),
        ('123veryLongName', False),
        ('123VeryLongName', False),
        ('VeryLongNameV123', True),
        ('VeryLongName123V', False),
        ('VeryLongName123Version', True),
        ('VeryLongName-veryLongName', False),
        ('VeryLongName-VeryLongName', True),
        ('VeryLongNameV123-VeryLongNameV123', True),
        ('VeryLongName123V-VeryLongName123V', False),
        ('VeryLongName123Version-VeryLongName123Version', True),
        ('-VeryLongName', False),
        ('-VeryLongName-VeryLongName', False),
        ('--VeryLongName-VeryLongName', False),
        ('-VeryLongName-veryLongName', False),
        ('-VeryLongNameV123-VeryLongNameV123', False),
        ('-VeryLongName123V-VeryLongName123V', False),
        ('-VeryLongName123Version-VeryLongName123Version', False),
    ],
)
def test_is_pascal_case_with_disallow_digits_false_and_separator_char(
    input, expected_result
):
    assert (
        is_pascal_case(
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
        ('VeryLongName', True),
        ('veryLongName', False),
        ('123veryLongName', False),
        ('123VeryLongName', False),
        ('VeryLongNameV123', False),
        ('VeryLongName123V', False),
        ('VeryLongName123Version', False),
        ('VeryLongName-veryLongName', False),
        ('VeryLongName-VeryLongName', True),
        ('VeryLongNameV123-VeryLongNameV123', False),
        ('VeryLongName123V-VeryLongName123V', False),
        ('VeryLongName123Version-VeryLongName123Version', False),
        ('-VeryLongName', True),
        ('-VeryLongName-VeryLongName', True),
        ('--VeryLongName-VeryLongName', False),
        ('-VeryLongName-veryLongName', False),
        ('-VeryLongNameV123-VeryLongNameV123', False),
        ('-VeryLongName123V-VeryLongName123V', False),
        ('-VeryLongName123Version-VeryLongName123Version', False),
    ],
)
def test_is_pascal_case_with_disallow_digits_true_and_separator_char_and_separator_allow_leading_true(
    input, expected_result
):
    assert (
        is_pascal_case(
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
        ('VeryLongName', True),
        ('veryLongName', False),
        ('123veryLongName', False),
        ('123VeryLongName', False),
        ('VeryLongNameV123', True),
        ('VeryLongName123V', False),
        ('VeryLongName123Version', True),
        ('VeryLongName-veryLongName', False),
        ('VeryLongName-VeryLongName', True),
        ('VeryLongNameV123-VeryLongNameV123', True),
        ('VeryLongName123V-VeryLongName123V', False),
        ('VeryLongName123Version-VeryLongName123Version', True),
        ('-VeryLongName', True),
        ('-VeryLongName-VeryLongName', True),
        ('--VeryLongName-VeryLongName', False),
        ('-VeryLongName-veryLongName', False),
        ('-VeryLongNameV123-VeryLongNameV123', True),
        ('-VeryLongName123V-VeryLongName123V', False),
        ('-VeryLongName123Version-VeryLongName123Version', True),
    ],
)
def test_is_pascal_case_with_disallow_digits_false_and_separator_char_and_separator_allow_leading_true(
    input, expected_result
):
    assert (
        is_pascal_case(
            input=input,
            disallow_digits=False,
            separator_char='-',
            separator_allow_leading=True,
        )
        is expected_result
    )
