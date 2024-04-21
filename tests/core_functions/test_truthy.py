import pytest

from oas_cli.core_functions.truthy import truthy


@pytest.mark.parametrize(
    'property_value, expected_error_count',
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
def test_truthy(property_value, expected_error_count):
    context = '$'
    target_value = {
        'myProperty': property_value
    }
    field_name = 'myProperty'
    errors = truthy(
        context=context,
        target_value=target_value,
        function_options=None,
        field_name=field_name,
    )
    assert len(errors) == expected_error_count
    if expected_error_count == 1:
        assert errors[0] == f'{context}.{field_name} must not be: empty string, 0, false, null'
