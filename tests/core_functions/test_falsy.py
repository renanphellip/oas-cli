import pytest
from oas_cli.core_functions.falsy import falsy


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        ('testing', 1),
        ('', 0),
        (123, 1),
        (0, 0),
        (True, 1),
        (False, 0),
        (None, 0)
    ],
)
def test_falsy(input, expected_errors):
    context = '$'
    target_value = {
        'myProperty': input
    }
    field_name = 'myProperty'
    errors = falsy(
        context=context,
        target_value=target_value,
        function_options=None,
        field_name=field_name,
    )
    assert len(errors) == expected_errors
