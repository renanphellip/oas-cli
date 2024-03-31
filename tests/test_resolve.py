import pytest
from oas_cli.resolve import resolve_external_references, resolve


@pytest.fixture
def mock_read_file(mocker):
    mock = mocker.patch('oas_cli.resolve.read_file')
    return mock


def test_resolve_external_references_dict(mock_read_file):
    mock_read_file.return_value = {'key': '$ref', '$ref': 'external.json'}
    base_path = '/testing_directory'
    data = {
        '$ref': '#/components/schemas/testing'
    }
    resolved_data = resolve_external_references(data, base_path)
    assert resolved_data == data


def test_resolve_external_references_list(mock_read_file):
    mock_read_file.return_value = {'key': '$ref', '$ref': 'external.json'}
    base_path = '/testing_directory'
    resolved_data = resolve_external_references([{'key': '$ref', '$ref': 'external.json'}], base_path)
    assert resolved_data == [{'key': {}, '$ref': 'external.json'}]


def test_resolve_external_references_nested_dict(mock_read_file):
    mock_read_file.return_value = {'nested_key': {'$ref': 'external.json'}}
    base_path = '/testing_directory'
    resolved_data = resolve_external_references({'nested_key': {'$ref': 'external.json'}}, base_path)
    assert resolved_data == {'nested_key': {'$ref': 'external.json'}}


def test_resolve_external_references_invalid_ref(mock_read_file):
    mock_read_file.return_value = None
    base_path = '/testing_directory'
    resolved_data = resolve_external_references({'key': '$ref', '$ref': '#internal'}, base_path)
    assert resolved_data == {'key': '$ref', '$ref': '#internal'}


def test_resolve_external_references_internal_ref(mock_read_file):
    mock_read_file.return_value = None
    base_path = '/testing_directory'
    resolved_data = resolve_external_references({'key': '$ref', '$ref': '#internal'}, base_path)
    assert resolved_data == {'key': '$ref', '$ref': '#internal'}


def test_resolve_contract_success(mock_read_file):
    mock_read_file.return_value = {'key': 'value'}
    contract_path = '/path/to/contract.json'
    resolved_data = resolve(contract_path)
    assert resolved_data == {'key': 'value'}


def test_resolve_contract_failure(mock_read_file, capsys):
    mock_read_file.side_effect = FileNotFoundError('File not found')
    contract_path = '/path/to/contract.json'
    with pytest.raises(SystemExit):
        resolve(contract_path)
    captured = capsys.readouterr()
    assert '[red]Failed to resolve the contract: File not found[/red]\n' in captured.out
