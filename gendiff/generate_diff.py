import os
from gendiff.make_ast import make_ast
from gendiff.parsers import get_parser
from gendiff.formatters.get_formatter import get_formatter


def read_file(filepath):
    with open(filepath) as f:
        content = f.read()
    return content


def generate_diff(file_path1, file_path2, format_name="stylish"):
    file_content1 = read_file(file_path1)
    file_content2 = read_file(file_path2)
    file_extension = os.path.splitext(file_path1)[1][1:]
    parse = get_parser(file_extension)

    obj1 = parse(file_content1)
    obj2 = parse(file_content2)

    ast = make_ast(obj1, obj2)
    formater = get_formatter(format_name)

    return formater(ast)
