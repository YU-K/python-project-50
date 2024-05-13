from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish


def get_formatter(format_name):
    match format_name:
        case 'plain':
            return plain
        case 'stylish':
            return stylish
        case _:
            raise Exception(f"Unknown format name {format_name}!")
