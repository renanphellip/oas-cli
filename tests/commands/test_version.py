import pytest

from oas_cli.commands.version import version


@pytest.fixture
def mock_read_file(mocker):
    mock = mocker.patch('oas_cli.commands.version.read_file')
    return mock


def test_version_with_valid_config_version(mock_read_file, capsys):
    mock_read_file.return_value = {
        'tool': {
            'poetry': {
                'version': '1.0.0'
            }
        }
    }
    version()
    out, _ = capsys.readouterr()
    assert 'OAS CLI version: 1.0.0' in out



def test_version_with_no_config_version(mock_read_file):
    mock_read_file.return_value = {}
    with pytest.raises(SystemExit):
        version()
