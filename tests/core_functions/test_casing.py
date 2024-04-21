import pytest

from oas_cli.core_functions.casing import casing


@pytest.mark.parametrize(
    'target_value, casing_type, expected_error_count',
    [
        ('flatcasestring', 'flat', 0),
        ('FlatCaseString', 'flat', 1),
        ('camelCaseString', 'camel', 0),
        ('CamelCaseString', 'camel', 1),
        ('PascalCaseString', 'pascal', 0),
        ('pascalCaseString', 'pascal', 1),
        ('kebab-case-string', 'kebab', 0),
        ('kebab_case_string', 'kebab', 1),
        ('COBOL-CASE-STRING', 'cobol', 0),
        ('COBOL_CASE_STRING', 'cobol', 1),
        ('snake_case_string', 'snake', 0),
        ('snake-case-string', 'snake', 1),
        ('MACRO_CASE_STRING', 'macro', 0),
        ('MACRO-CASE-STRING', 'macro', 1),
    ],
)
def test_casing(target_value, casing_type, expected_error_count):
    context = '$.info.title'
    target_value = target_value
    function_options = {
        'type': casing_type
    }
    field_name = 'tags'
    errors = casing(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=field_name,
    )
    assert len(errors) == expected_error_count
    if len(errors) == 1:
        assert errors[0] == f'{context} must be {casing_type} case.'
