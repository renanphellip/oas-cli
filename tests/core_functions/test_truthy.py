import pytest
from oas_cli.core_functions.truthy import truthy


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        ('testing', 0),
        ('', 1),
        (123, 0),
        (0, 1),
        (True, 0),
        (False, 1),
        (None, 1)
    ],
)
def test_truthy(input, expected_errors):
    context = '$'
    target_value = {
        'myProperty': input
    }
    field_name = 'myProperty'
    errors = truthy(
        context=context,
        target_value=target_value,
        function_options=None,
        field_name=field_name,
    )
    assert len(errors) == expected_errors
