import pytest
from oas_cli.core_functions.undefined import undefined


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        ('testing', 1),
        ('', 1),
        (123, 1),
        (0, 1),
        (True, 1),
        (False, 1),
        (None, 0)
    ],
)
def test_undefined(input, expected_errors):
    context = '$'
    target_value = {
        'myProperty': input
    }
    field_name = 'myProperty'
    errors = undefined(
        context=context,
        target_value=target_value,
        function_options=None,
        field_name=field_name,
    )
    assert len(errors) == expected_errors
