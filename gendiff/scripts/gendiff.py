#!/usr/bin/env python
import argparse
import os
import yaml
from gendiff.generate_diff import generate_diff
from gendiff.parsers import get_parser
from gendiff.formatters.get_formatter import get_formatter

arg_parser = argparse.ArgumentParser(
    description='Compares two configuration '
                'files and shows a difference.')
arg_parser.add_argument('first_file')
arg_parser.add_argument('second_file')
arg_parser.add_argument('-f', '--format',
                        default='stylish',
                        help='set format of output (default: stylish)')

args = arg_parser.parse_args()
format_name = get_formatter(args.format)

file_extension = os.path.splitext(args.first_file)[1][1:]

# TODO: создать функцию get_filepath  -
#  получить путь до файла
# TODO: создать функцию get_file_content -
#  читает файл и возвращает данные из файла
# TODO: создать функцию parse -
#  парсит данные из файла в объекты, которые поддерживает ЯП

# TODO: Добавьте текущий форматер как форматер по умолчанию для библиотеки.
#       Это значит, что данный форматер применяется,
#       если не указан какой-то другой
# TODO: Укажите stylish как форматер по умолчанию в исполняемом файле
# TODO: Добавьте в ридми аскинему с примером работы пакета c yaml


first_file_path = f"{os.getcwd()}/{args.first_file}"
second_file_path = f"{os.getcwd()}/{args.second_file}"

with open(first_file_path) as first_file_path1:
    with open(second_file_path) as second_file_path1:
        parser = get_parser(file_extension)
        if parser == yaml:
            data1 = parser.load(first_file_path1, Loader=yaml.Loader)
            data2 = parser.load(second_file_path1, Loader=yaml.Loader)
        else:
            data1 = parser.load(first_file_path1)
            data2 = parser.load(second_file_path1)


def main():
    # diff = generate_diff(data1, data2, plain)
    diff = generate_diff(data1, data2, format_name)
    print(diff)


if __name__ == "main":
    main()
