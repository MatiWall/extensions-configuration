from dataclasses import dataclass, make_dataclass
from pathlib import Path
from typing import Union, Any

import yaml

FILE_NAMES = [
    'secrets.yaml', 'secrets.yaml',
    'appconfig.yml', 'appconfig.yaml',
    'appconfig.Production.yml', 'appconfig.Production.yaml'
]

def read_configs_to_dataclass(path: Path = Path.cwd()):
    configs = read_configs(path)
    appconfig = make_dataclass_from_config(configs)
    return appconfig
def read_configs(
        path: Path = Path.cwd(),
):
    config_data = []

    for file_name in FILE_NAMES:
        file_path = path / file_name

        if file_path.is_file():
            with open(file_path, 'r') as file:
                config_data.append(yaml.safe_load(file))

    return config_data

def make_dataclass_from_config(config: Union[list, tuple, dict], class_name: str = 'AppConfig'):
    fields_list = []

    if isinstance(config, (dict,)):
        config = [config]

    _config = {}
    for c in config:
        _config.update(c)

    for key, value in _config.items():
        if isinstance(value, dict):
            nested_class_name = key.capitalize() + "Data"
            nested_dataclass = make_dataclass_from_config(value, nested_class_name)
            fields_list.append((key, Union[nested_dataclass, Any]))
        else:
            fields_list.append((key, Any))

    return make_dataclass(class_name, fields_list)