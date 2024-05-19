import json
import yaml


def get_parser(file_extension):
    match file_extension:
        case 'json':
            return json.loads
        case 'yml' | 'yaml':
            return yaml.safe_load
        case _:
            raise Exception(f"Unknown format name {file_extension}!")
