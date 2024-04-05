import pytest
from oas_cli.core_functions.unreferenced_reusable_object import unreferencedReusableObject


@pytest.mark.parametrize(
    'target_value, reusable_objects_location, expected_error_count',
    [
        (
            {'$ref': '#/components/schema/xpto'},\
            '#/components/schema/xpto',
            0
        ),
        (
            {'key': 'value'},
            '#/components/schema/xpto',
            1
        ),
        (
            {'nested': {'$ref': '#/components/schema/xpto'}},
            '#/components/schema/xpto',
            0
        ),
        (
            {'nested': [{'$ref': '#/components/schema/xpto'}]},
            '#/components/schema/xpto',
            0
        ),
        (
            [{'$ref': '#/components/schema/xpto'}],
            '#/components/schema/xpto',
            0
        ),
        (
            ['value'],
            '#/components/schema/xpto',
            1
        ),
        (
            '#/components/schema/xpto',
            '#/components/schema/xpto',
            0
        ),
        (
            'not_a_ref',
            '#/components/schema/xpto',
            1
        )
    ]
)
def test_unreferenced_reusable_object(target_value, reusable_objects_location, expected_error_count):
    context = '$'
    function_options = {
        'reusableObjectsLocation': reusable_objects_location
    }
    errors = unreferencedReusableObject(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=None,
    )
    assert len(errors) == expected_error_count
    if len(errors) == 1:
        assert errors[0] == f'No reference to {reusable_objects_location} was found in {context}.'
