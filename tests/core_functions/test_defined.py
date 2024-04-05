import pytest
from oas_cli.core_functions.defined import defined


@pytest.mark.parametrize(
    'property_value, expected_error_count',
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
def test_defined(property_value, expected_error_count):
    context = '$'
    target_value = {
        'myProperty': property_value
    }
    field_name = 'myProperty'
    errors = defined(
        context=context,
        target_value=target_value,
        function_options=None,
        field_name=field_name,
    )
    assert len(errors) == expected_error_count
    if len(errors) == 1:
        assert errors[0] == f'{context}.{field_name} must not be null.'
