import pytest
from oas_cli.core_functions.schema import schema


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        ([1], 1),
        ([1, 2], 0),
        ([1, 2, 3], 0),
        ([1, 2, 3, 4], 0),
        ([1, 2, 3, 4, 5], 1),
    ],
)
def test_schema_with_dialect_auto(input, expected_errors):
    context = '$'
    target_value = {
        'myProperty': input
    }
    function_options = {
        'schema': {
            'type': 'array',
            'minItems': 2,
            'maxItems': 4,
            'items': {
                'type': 'number'
            }
        }
    }
    field_name = 'myProperty'
    errors = schema(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=field_name,
    )
    assert len(errors) == expected_errors
    if expected_errors > 0:
        assert errors[0] == f'{context}.{field_name} does not meet the expected schema: {function_options.get('schema')}'


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        (['a'], 1),
        (['a', 'b'], 0),
        (['a', 'b', 'c'], 0),
        (['a', 'b', 'c', 'd'], 0),
        (['a', 'b', 'c', 'd', 'e'], 1),
    ],
)
def test_schema_with_dialect_auto_and_return_all_errors(input, expected_errors):
    context = '$'
    target_value = {
        'myProperty': input
    }
    function_options = {
        'schema': {
            'type': 'array',
            'minItems': 2,
            'maxItems': 4,
            'items': {
                'type': 'string'
            }
        },
        'allErrors': True
    }
    field_name = 'myProperty'
    errors = schema(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=field_name,
    )
    assert len(errors) == expected_errors
    if expected_errors > 0:
        assert errors[0] != f'{context}.{field_name} does not meet the expected schema: {function_options.get('schema')}'


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        (['a'], 1),
        (['a', 'b'], 0),
        (['a', 'b', 'c'], 0),
        (['a', 'b', 'c', 'd'], 0),
        (['a', 'b', 'c', 'd', 'e'], 1),
    ],
)
def test_schema_with_dialect_draft4_and_return_all_errors(input, expected_errors):
    context = '$'
    target_value = {
        'myProperty': input
    }
    function_options = {
        'schema': {
            'type': 'array',
            'minItems': 2,
            'maxItems': 4,
            'items': {
                'type': 'string'
            }
        },
        'dialect': 'draft4',
        'allErrors': True
    }
    field_name = 'myProperty'
    errors = schema(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=field_name,
    )
    assert len(errors) == expected_errors
    if expected_errors > 0:
        assert errors[0] != f'{context}.{field_name} does not meet the expected schema: {function_options.get('schema')}'


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        (['a'], 1),
        (['a', 'b'], 0),
        (['a', 'b', 'c'], 0),
        (['a', 'b', 'c', 'd'], 0),
        (['a', 'b', 'c', 'd', 'e'], 1),
    ],
)
def test_schema_with_dialect_draft6_and_return_all_errors(input, expected_errors):
    context = '$'
    target_value = {
        'myProperty': input
    }
    function_options = {
        'schema': {
            'type': 'array',
            'minItems': 2,
            'maxItems': 4,
            'items': {
                'type': 'string'
            }
        },
        'dialect': 'draft6',
        'allErrors': True
    }
    field_name = 'myProperty'
    errors = schema(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=field_name,
    )
    assert len(errors) == expected_errors
    if expected_errors > 0:
        assert errors[0] != f'{context}.{field_name} does not meet the expected schema: {function_options.get('schema')}'


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        (['a'], 1),
        (['a', 'b'], 0),
        (['a', 'b', 'c'], 0),
        (['a', 'b', 'c', 'd'], 0),
        (['a', 'b', 'c', 'd', 'e'], 1),
    ],
)
def test_schema_with_dialect_draft7_and_return_all_errors(input, expected_errors):
    context = '$'
    target_value = {
        'myProperty': input
    }
    function_options = {
        'schema': {
            'type': 'array',
            'minItems': 2,
            'maxItems': 4,
            'items': {
                'type': 'string'
            }
        },
        'dialect': 'draft7',
        'allErrors': True
    }
    field_name = 'myProperty'
    errors = schema(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=field_name,
    )
    assert len(errors) == expected_errors
    if expected_errors > 0:
        assert errors[0] != f'{context}.{field_name} does not meet the expected schema: {function_options.get('schema')}'


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        (['a'], 1),
        (['a', 'b'], 0),
        (['a', 'b', 'c'], 0),
        (['a', 'b', 'c', 'd'], 0),
        (['a', 'b', 'c', 'd', 'e'], 1),
    ],
)
def test_schema_with_dialect_draft2019_09_and_return_all_errors(input, expected_errors):
    context = '$'
    target_value = {
        'myProperty': input
    }
    function_options = {
        'schema': {
            'type': 'array',
            'minItems': 2,
            'maxItems': 4,
            'items': {
                'type': 'string'
            }
        },
        'dialect': 'draft2019-09',
        'allErrors': True
    }
    field_name = 'myProperty'
    errors = schema(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=field_name,
    )
    assert len(errors) == expected_errors
    if expected_errors > 0:
        assert errors[0] != f'{context}.{field_name} does not meet the expected schema: {function_options.get('schema')}'


@pytest.mark.parametrize(
    'input, expected_errors',
    [
        (['a'], 1),
        (['a', 'b'], 0),
        (['a', 'b', 'c'], 0),
        (['a', 'b', 'c', 'd'], 0),
        (['a', 'b', 'c', 'd', 'e'], 1),
    ],
)
def test_schema_with_dialect_draft2020_12_and_return_all_errors(input, expected_errors):
    context = '$'
    target_value = {
        'myProperty': input
    }
    function_options = {
        'schema': {
            'type': 'array',
            'minItems': 2,
            'maxItems': 4,
            'items': {
                'type': 'string'
            }
        },
        'dialect': 'draft2020-12',
        'allErrors': True
    }
    field_name = 'myProperty'
    errors = schema(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=field_name,
    )
    assert len(errors) == expected_errors
    if expected_errors > 0:
        assert errors[0] != f'{context}.{field_name} does not meet the expected schema: {function_options.get('schema')}'
