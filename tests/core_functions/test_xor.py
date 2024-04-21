import pytest

from oas_cli.core_functions.xor import xor


@pytest.mark.parametrize(
    'target_value, properties, expected_error_count',
    [
        (
            {'x': 1},
            ['x', 'y', 'z'],
            0
        ),
        (
            {'a': 1, 'b': 2, 'c': 3, 'y': 4},
            ['x', 'y', 'z'],
            0
        ),
        (
            {'a': 1, 'b': 2, 'c': 3, 'y': 4, 'z': 5},
            ['x', 'y', 'z'],
            1
        ),
        (
            {'a': 1, 'b': 2, 'c': 3},
            ['x', 'y', 'z'],
            1
        ),
    ]
)
def test_xor(target_value, properties, expected_error_count):
    context = '$.components.examples.*'
    errors = xor(
        context=context,
        target_value=target_value,
        function_options={
            'properties': properties
        },
        field_name=None,
    )
    assert len(errors) == expected_error_count
    if len(errors) == 1:
        assert errors[0] == f'{context} must have only one of these properties defined: {properties}'
