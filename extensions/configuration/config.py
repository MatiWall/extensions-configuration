from dataclasses import dataclass, fields
from pathlib import Path
from typing import Type, Dict, Any

import yaml

# List of configuration file names to look for
FILE_NAMES = [
    'appconfig.yml', 'appconfig.yaml',
    'appconfig.Production.yml', 'appconfig.Production.yaml',
    'secrets.yaml'
]

def read_configs(path: Path = Path.cwd()) -> Dict[str, Any]:
    """ Read and merge YAML configuration files.

    Parameters
    ----------
    path : Path, optional
        Directory containing configuration files (default is current working directory).

    Returns
    -------
    dict
        Combined configuration data as a dictionary.
    """
    config_data = {}

    for file_name in FILE_NAMES:
        file_path = path / file_name

        if file_path.is_file():
            try:
                with open(file_path, 'r') as file:
                    file_data = yaml.safe_load(file) or {}
                    config_data.update(file_data)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    return config_data

def read_configs_to_dataclass(klass: Type[dataclass], path: Path = Path.cwd()) -> dataclass:
    """Construct a dataclass instance from configuration files.

    Parameters
    ----------
    klass : Type[dataclass]
        The dataclass type to instantiate.

    path : Path, optional
        Directory containing configuration files (default is current working directory).

    Returns
    -------
    dataclass
        Dataclass instance constructed from the combined configuration data.
    """
    config = read_configs(path)
    return make_dataclass_from_config(klass, config)

def make_dataclass_from_config(klass: Type[dataclass], config: Dict[str, Any]) -> dataclass:
    """Create a dataclass instance from a dictionary of configuration data.

    Parameters
    ----------
    klass : Type[dataclass]
        The dataclass type to instantiate.

    config : Dict[str, Any]
        The configuration data.

    Returns
    -------
    dataclass
        An instance of the dataclass populated with the configuration data.
    """
    field_names = {field.name for field in fields(klass)}
    filtered_config = {k: v for k, v in config.items() if k in field_names}
    return klass(**filtered_config)
