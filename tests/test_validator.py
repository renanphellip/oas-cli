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
        'y': ['y'],
        'z': {
            'a': 'a'
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
    results = validator._Validator__get_jsonpath_results(given, data)
    
    assert isinstance(results, list) is True
    assert len(results) == 1

    result = results[0]
    assert isinstance(result, JSONPathResult)
    assert result.context == given
    assert result.target_value == data