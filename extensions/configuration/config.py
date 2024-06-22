"""Configuration

This module handles the reading of configfiles and the creation of a config object.
It looks for the files appconfig.yaml, appconfig.Production.yaml and secrets.yaml. If the same key is available in more
than one file it follows the same hierarchy as the order of the just mentioned files.
"""

from dataclasses import dataclass, make_dataclass
from pathlib import Path
from typing import Union, Any

import yaml

FILE_NAMES = [
    'appconfig.yml', 'appconfig.yaml',
    'appconfig.Production.yml', 'appconfig.Production.yaml',
    'secrets.yaml', 'secrets.yaml',
]

def read_configs_to_dataclass(path: Path = Path.cwd()) -> Any:
    """Construct config object
    Reads configuration files and constructs a dataclass instance.

    Parameters
    ----------
    path : Path, optional
        Directory containing configuration files (default is current working directory).

    Returns
    -------
    Any
        Dataclass instance constructed from the combined configuration data.
    """

    config = read_configs(path)
    appconfig = make_dataclass_from_config(config)
    return appconfig
def read_configs(
        path: Path = Path.cwd(),
) -> dict:
    """ Read Configs
    Reads and merges YAML configuration files.

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
            with open(file_path, 'r') as file:
                config_data.update(yaml.safe_load(file))

    return config_data

def make_dataclass_from_config(config: dict, class_name: str = 'AppConfig') -> type:
    """
    Dynamically creates a dataclass from a nested dictionary configuration.

    Parameters
    ----------
    config : dict
        Nested dictionary configuration.
    class_name : str, optional
        Name for the top-level dataclass (default is 'AppConfig').

    Returns
    -------
    type
        Dynamically generated dataclass type based on the configuration.
    """
    fields_list = []


    for key, value in config.items():
        if isinstance(value, dict):
            nested_class_name = key.capitalize() + "Data"
            nested_dataclass = make_dataclass_from_config(value, nested_class_name)
            fields_list.append((key, Union[Any]))
        else:
            fields_list.append((key, Any))

    return make_dataclass(class_name, fields_list)(**config)