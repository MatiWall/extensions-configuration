import pytest
from extensions.configuration import read_configs_to_dataclass

@pytest.fixture
def test_config(tmp_path):
    # Prepare a temporary directory with test YAML files
    config_path = tmp_path / 'test_configs'
    config_path.mkdir()

    yaml_data = """
    key1: value1
    key2:
        nested_key1: nested_value1
        nested_key2: nested_value2
    """

    for file_name in ['secrets.yaml', 'appconfig.yaml']:
        with open(config_path / file_name, 'w') as file:
            file.write(yaml_data)

    return config_path

def test_read_configs_to_dataclass(test_config):
    appconfig = read_configs_to_dataclass(test_config)

    # Ensure that the dataclass is created successfully
    assert appconfig is not None

    # You may add more specific assertions based on your dataclass structure
    # For example, check if specific fields are present or have expected values
    assert hasattr(appconfig, 'key1')
    assert hasattr(appconfig, 'key2')
