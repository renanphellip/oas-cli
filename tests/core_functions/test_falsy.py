import pytest

from oas_cli.core_functions.falsy import falsy


@pytest.mark.parametrize(
    'property_value, expected_error_count',
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
def test_falsy(property_value, expected_error_count):
    context = '$'
    target_value = {
        'myProperty': property_value
    }
    field_name = 'myProperty'
    errors = falsy(
        context=context,
        target_value=target_value,
        function_options=None,
        field_name=field_name,
    )
    assert len(errors) == expected_error_count
    if len(errors) == 1:
        assert errors[0] == f'{context}.{field_name} must be: empty string, 0, false, null'