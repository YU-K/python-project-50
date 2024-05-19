from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.formatters.json_format import json_format


def get_formatter(format_name):
    match format_name:
        case 'plain':
            return plain
        case 'stylish':
            return stylish
        case 'json':
            return json_format
        case _:
            raise Exception(f"Unknown format name {format_name}!")
