from dataclasses import dataclass, make_dataclass
from pathlib import Path
from typing import Union, Any

import yaml

FILE_NAMES = [
    'secrets.yaml', 'secrets.yaml',
    'appconfig.Production.yml', 'appconfig.Production.yaml',
    'appconfig.yml', 'appconfig.yaml',
]

def read_configs_to_dataclass(path: Path = Path.cwd()):
    config = read_configs(path)
    appconfig = make_dataclass_from_config(config)
    return appconfig
def read_configs(
        path: Path = Path.cwd(),
):
    config_data = {}

    for file_name in FILE_NAMES:
        file_path = path / file_name

        if file_path.is_file():
            with open(file_path, 'r') as file:
                config_data.update(yaml.safe_load(file))

    return config_data

def make_dataclass_from_config(config: Union[list, tuple, dict], class_name: str = 'AppConfig'):
    fields_list = []


    for key, value in config.items():
        if isinstance(value, dict):
            nested_class_name = key.capitalize() + "Data"
            nested_dataclass = make_dataclass_from_config(value, nested_class_name)
            fields_list.append((key, Union[Any]))
        else:
            fields_list.append((key, Any))

    return make_dataclass(class_name, fields_list)(**config)