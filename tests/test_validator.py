import pytest
from oas_cli.validate import Validator
from oas_cli.entities.custom import JSONPathResult

@pytest.fixture
def validator():
    return Validator()

@pytest.fixture
def data():
    return {
        'x': 'x',
        'y': [
            {
                'xpto': 'a'
            },
            {
                'xpto': 'b'
            }
        ],
        'z': {
            'abc': 'abc'
        }
    }

def test_get_jsonpath_results_exception_with_invalid_given(validator, data, capsys):
    given = '#'
    with pytest.raises(SystemExit) as excinfo:
        validator._Validator__get_jsonpath_results(given, data)
    captured = capsys.readouterr()
    assert f'Failed to parse JSONPath "{given}"' in captured.out
    assert excinfo.type == SystemExit
    assert excinfo.value.code == 1

def test_get_jsonpath_results_with_root_string(validator, data):
    given = '$'
    expected_results = 1
    target_value = data
    results = validator._Validator__get_jsonpath_results(given, data)
    assert isinstance(results, list) is True
    assert len(results) == expected_results
    assert isinstance(results[0], JSONPathResult)
    assert results[0].context == given
    assert results[0].target_value == target_value

@pytest.mark.parametrize(
    'given, expected_results, target_value',
    [
        ('$.x', 1, 'x'),
        ('y', 1, [{'xpto': 'a'}, {'xpto': 'b'}]),
        ('$..abc', 1, 'abc'),
        ('$.z~', 1, 'z'),
        ('$.y[*].xpto', 2, ('a', 'b')),
    ],
)
def test_get_jsonpath_results_with_valid_given(validator, data, given, expected_results, target_value):
    results = validator._Validator__get_jsonpath_results(given, data)
    assert isinstance(results, list) is True
    assert len(results) == expected_results
    if len(results) > 0:
        for i in range(len(results)):
            assert isinstance(results[i], JSONPathResult)
            new_target_value = target_value[i] if isinstance(target_value, tuple) else target_value
            assert results[i].target_value == new_target_value

@pytest.mark.parametrize(
    "error_messages, old_value, new_value, expected_messages",
    [
        (
            [
                "An error occurred in {{path}}",
                "{{path}} is invalid"
            ],
            "{{path}}",
            "/examples/{exampleId}",
            [
                "An error occurred in /examples/{exampleId}",
                "/examples/{exampleId} is invalid"
            ]
        ),
        (
            [
                "'{{property}}' is required",
                "Invalid value to '{{property}}'"
            ],
            "{{property}}",
            "title",
            [
                "'title' is required",
                "Invalid value to 'title'"
            ]
        ),
        (
            [
                "'{{value}}' is not a dict",
                "The value '{{value}}' is valid"
            ],
            "{{value}}",
            "123",
            [
                "'123' is not a dict",
                "The value '123' is valid"
            ]
        ),
    ]
)
def test_replace_messages(validator, error_messages, old_value, new_value, expected_messages):
    assert validator._Validator__replace_messages(error_messages, old_value, new_value) == expected_messages

