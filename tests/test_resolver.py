import pytest
from pytest_mock import MockerFixture

from oas_cli.resolver import Resolver


@pytest.fixture
def resolver():
    return Resolver()

@pytest.fixture
def mocked_read_file(mocker: MockerFixture):
    return mocker.patch('oas_cli.resolver.read_file')


def test_resolve_external_references_dict(mocked_read_file, resolver):
    data = {
        '$ref': 'a.yaml',
        'b': {
            '$ref': 'c.yaml'
        },
        'd': {
            '$ref': '#/components/schemas/d'
        }
    }
    mocked_read_file.side_effect = [
        {'a': 'a'},
        {'c': 'c'}
    ]
    resolved_data = resolver._Resolver__resolve_external_references(data, '/base/path')
    assert resolved_data == {
        'a': 'a',
        'b': {
            'c': 'c'
        },
        'd': {
            '$ref': '#/components/schemas/d'
        }
    }
    mocked_read_file.assert_any_call('/base/path/a.yaml', resolver.verbose)
    mocked_read_file.assert_any_call('/base/path/c.yaml', resolver.verbose)
    assert mocked_read_file.call_count == 2

def test_resolve_external_references_list(mocked_read_file, resolver):
    data = [
        {"$ref": "a.yaml"},
        {"$ref": "b.yaml"}
    ]
    mocked_read_file.side_effect = [
        {"a": "a"},
        {"b": "b"}
    ]
    resolved_data = resolver._Resolver__resolve_external_references(data, "/base/path")
    assert resolved_data == [
        {"a": "a"},
        {"b": "b"}
    ]
    mocked_read_file.assert_any_call("/base/path/a.yaml", resolver.verbose)
    mocked_read_file.assert_any_call("/base/path/b.yaml", resolver.verbose)
    assert mocked_read_file.call_count == 2

def test_resolve(mocked_read_file, resolver):
    mocked_read_file.return_value = {
        "key": "value"
    }
    resolved_data = resolver.resolve("/base/path/contract.yaml")
    assert resolved_data == {"key": "value"}
    mocked_read_file.assert_called_once_with("/base/path/contract.yaml", resolver.verbose)

def test_resolve_exception(mocked_read_file, resolver, capsys):
    mocked_read_file.side_effect = Exception("Error")
    with pytest.raises(SystemExit) as excinfo:
        resolver.resolve("/base/path/contract.yaml")
    captured = capsys.readouterr()
    assert 'Failed to resolve the contract' in captured.out
    assert excinfo.type == SystemExit
    assert excinfo.value.code == 1
