import json
import yaml


def get_parser(file_extension):
    if file_extension == 'json':
        return json
    elif file_extension in ['yml', 'yaml']:
        return yaml
