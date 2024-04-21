import pytest

from oas_cli.entities.rulesets import Severity
from oas_cli.rulesets import get_rules


@pytest.fixture
def mock_read_file(mocker):
    mock = mocker.patch('oas_cli.rulesets.read_file')
    return mock


def test_get_rules_with_valid_rulesets(mock_read_file):
    mock_read_file.return_value = {
        'rules': {
            'first-rule': {
                'description': 'testing',
                'message': 'testing',
                'documentation': 'testing',
                'given': '$.testing',
                'severity': 'error',
                'then': {
                    'function': 'testing',
                    'functionOptions': {'testing': 'testing'},
                },
            },
            'second-rule': {
                'description': 'testing',
                'message': 'testing',
                'given': '$.testing',
                'severity': 'error',
                'then': {
                    'function': 'testing',
                    'functionOptions': {'testing': 'testing'},
                },
            },
        }
    }
    try:
        get_rules('mocked_path')
    except SystemExit:
        pytest.fail('The function raised SystemExit, but it should not have.')


def test_get_rules_with_valid_rulesets_and_multiple_properties_value(
    mock_read_file,
):
    mock_read_file.return_value = {
        'rules': {
            'first-rule': {
                'description': 'testing',
                'message': ['testing1', 'testing2'],
                'documentation': [
                    'testing1',
                    'testing2',
                ],
                'given': [
                    '$.testing[1]',
                    '$.testing[2]',
                ],
                'severity': 'error',
                'then': {
                    'function': 'testing',
                    'functionOptions': {'testing': 'testing'},
                },
            }
        }
    }
    try:
        get_rules('mocked_path')
    except SystemExit:
        pytest.fail('The function raised SystemExit, but it should not have.')


def test_get_rules_with_valid_rulesets_and_new_properties(
    mock_read_file,
):
    mock_read_file.return_value = {
        'rules': {
            'first-rule': {
                'description': 'testing',
                'message': 'testing',
                'documentation': 'testing',
                'given': '$.testing',
                'severity': 'error',
                'then': {
                    'function': 'testing',
                    'functionOptions': {'testing': 'testing'},
                },
                'xpto': 'testing',
            }
        }
    }
    try:
        get_rules('mocked_path')
    except SystemExit:
        pytest.fail('The function raised SystemExit, but it should not have.')


def test_get_rules_with_invalid_rulesets(mock_read_file):
    mock_read_file.return_value = {'invalid_data': {}}
    with pytest.raises(SystemExit):
        get_rules('mocked_path')


def test_get_rules(mock_read_file):
    mock_read_file.return_value = {
        'rules': {
            'first-rule': {
                'description': 'testing',
                'message': 'testing',
                'documentation': 'testing',
                'given': '$.testing',
                'severity': 'error',
                'then': {
                    'field': 'testing',
                    'function': 'testing',
                    'functionOptions': {'testing': 'testing'},
                },
            }
        }
    }
    rules = get_rules('mocked_path')
    assert len(rules) == 1
    assert rules[0].name == 'first-rule'
    assert rules[0].description == 'testing'
    assert rules[0].message == 'testing'
    assert rules[0].severity == Severity.ERROR
    assert rules[0].given == '$.testing'
    assert rules[0].then.function == 'testing'
    assert rules[0].then.function_options == {'testing': 'testing'}
