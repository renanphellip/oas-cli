import pytest
from oas_cli.core_functions.defined import defined


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        ('testing', 0),
        ('', 0),
        (123, 0),
        (0, 0),
        (True, 0),
        (False, 0),
        (None, 1)
    ],
)
def test_defined(input, expected_errors):
    context = '$'
    target_value = {
        'myProperty': input
    }
    field_name = 'myProperty'
    errors = defined(
        context=context,
        target_value=target_value,
        function_options=None,
        field_name=field_name,
    )
    assert len(errors) == expected_errors
