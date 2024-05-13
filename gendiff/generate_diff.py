from gendiff.make_ast import make_ast
from gendiff.formatters.stylish import stylish


def generate_diff(filepath1, filepath2, format_name=stylish):
    ast = make_ast(filepath1, filepath2)
    return format_name(ast)
