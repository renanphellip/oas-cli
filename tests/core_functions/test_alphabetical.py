import pytest
from oas_cli.core_functions.alphabetical import alphabetical

@pytest.mark.parametrize(
    'target_value, field_name, keyed_by, expected_error_count',
    [
        (
            {
                'tags': [
                    {
                        'name': 'a',
                        'description': 'testing'
                    },
                    {
                        'name': 'b',
                        'description': 'testing'
                    },
                    {
                        'name': 'c',
                        'description': 'testing'
                    }
                ]
            },
            'tags',
            'name',
            0
        ),
        (
            {
                'tags': [
                    {
                        'name': 'b',
                        'description': 'testing'
                    },
                    {
                        'name': 'a',
                        'description': 'testing'
                    },
                    {
                        'name': 'c',
                        'description': 'testing'
                    }
                ]
            },
            'tags',
            'name',
            1
        ),
        (
            {
                'tags': [
                    {
                        'name': 'b',
                        'description': 'x testing'
                    },
                    {
                        'name': 'a',
                        'description': 'z testing'
                    },
                    {
                        'name': 'c',
                        'description': 'z testing'
                    }
                ]
            },
            'tags',
            'description',
            0
        ),
    ],
)
def test_alphabetical(target_value, field_name, keyed_by, expected_error_count):
    context = '$'
    target_value = target_value
    function_options = {
        'keyedBy': keyed_by
    }
    field_name = 'tags'
    errors = alphabetical(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=field_name,
    )
    assert len(errors) == expected_error_count
    if len(errors) == 1:
        assert errors[0] == f'{context} should have alphabetical {field_name} by {keyed_by}.'
