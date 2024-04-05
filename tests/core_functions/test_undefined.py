import pytest
from oas_cli.core_functions.undefined import undefined


@pytest.mark.parametrize(
    'property_value, expected_error_count',
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
def test_undefined(property_value, expected_error_count):
    context = '$'
    target_value = {
        'myProperty': property_value
    }
    field_name = 'myProperty'
    errors = undefined(
        context=context,
        target_value=target_value,
        function_options=None,
        field_name=field_name,
    )
    assert len(errors) == expected_error_count
    if len(errors) == 1:
        assert errors[0] == f'{context}.{field_name} must be null.'
