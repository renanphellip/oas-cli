import pytest
from oas_cli.entities import Severity
from oas_cli.ruleset import validate_ruleset_integrity, get_ruleset


@pytest.fixture
def mock_read_file(mocker):
    mock = mocker.patch('oas_cli.ruleset.read_file')
    return mock


def test_validate_ruleset_integrity_with_valid_ruleset(mock_read_file):
    mock_read_file.return_value = {
        "rules": {
            "first-rule": {
                "description": "testing",
                "message": "testing",
                "documentation": "testing",
                "given": "$.testing",
                "severity": "error",
                "then": {
                    "function": "testing",
                    "functionOptions": {
                        "testing": "testing"
                    }
                }
            },
            "second-rule": {
                "description": "testing",
                "message": "testing",
                "given": "$.testing",
                "severity": "error",
                "then": {
                    "function": "testing",
                    "functionOptions": {
                        "testing": "testing"
                    }
                }
            }
        }
    }
    assert validate_ruleset_integrity('mocked_path') == True


def test_validate_ruleset_integrity_with_valid_ruleset_and_multiple_properties_value(mock_read_file):
    mock_read_file.return_value = {
        "rules": {
            "first-rule": {
                "description": "testing",
                "message": [
                    "testing1",
                    "testing2"
                ],
                "documentation": [
                    "testing1",
                    "testing2",
                ],
                "given": [
                    "$.testing[1]",
                    "$.testing[2]",
                ],
                "severity": "error",
                "then": {
                    "function": "testing",
                    "functionOptions": {
                        "testing": "testing"
                    }
                }
            }
        }
    }
    assert validate_ruleset_integrity('mocked_path') == True


def test_validate_ruleset_integrity_with_valid_ruleset_and_new_properties(mock_read_file):
    mock_read_file.return_value = {
        "rules": {
            "first-rule": {
                "description": "testing",
                "message": "testing",
                "documentation": "testing",
                "given": "$.testing",
                "severity": "error",
                "then": {
                    "function": "testing",
                    "functionOptions": {
                        "testing": "testing"
                    }
                },
                "xpto": "testing"
            }
        }
    }
    assert validate_ruleset_integrity('mocked_path') == True


def test_validate_ruleset_integrity_with_invalid_ruleset(mock_read_file):
    mock_read_file.return_value = {'invalid_data': {}}
    with pytest.raises(SystemExit):
        validate_ruleset_integrity('mocked_path')


def test_get_ruleset(mock_read_file):
    mock_read_file.return_value = {
        "rules": {
            "first-rule": {
                "description": "testing",
                "message": "testing",
                "documentation": "testing",
                "given": "$.testing",
                "severity": "error",
                "then": {
                    "function": "testing",
                    "functionOptions": {
                        "testing": "testing"
                    }
                }
            }
        }
    }
    ruleset = get_ruleset('mocked_path')
    assert len(ruleset) == 1
    assert ruleset[0].name == 'first-rule'
    assert ruleset[0].description == 'testing'
    assert ruleset[0].message == 'testing'
    assert ruleset[0].severity == Severity.ERROR
    assert ruleset[0].given == '$.testing'
    assert ruleset[0].then.function == 'testing'
    assert ruleset[0].then.functionOptions == {'testing': 'testing'}
