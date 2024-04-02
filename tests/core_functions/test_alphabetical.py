from oas_cli.core_functions.alphabetical import alphabetical


def test_alphabetical_valid_tags_sorted_by_name():
    context = '$'
    target_value = {
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
    }
    function_options = {
        'keyedBy': 'name'
    }
    field_name = 'tags'
    errors = alphabetical(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=field_name,
    )
    assert len(errors) == 0


def test_alphabetical_invalid_tags_sorted_by_name():
    context = '$'
    target_value = {
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
    }
    function_options = {
        'keyedBy': 'name'
    }
    field_name = 'tags'
    errors = alphabetical(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=field_name,
    )
    assert len(errors) == 1


def test_alphabetical_valid_tags_sorted_by_description():
    context = '$'
    target_value = {
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
    }
    function_options = {
        'keyedBy': 'description'
    }
    field_name = 'tags'
    errors = alphabetical(
        context=context,
        target_value=target_value,
        function_options=function_options,
        field_name=field_name,
    )
    assert len(errors) == 0
