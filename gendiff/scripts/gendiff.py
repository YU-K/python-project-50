#!/usr/bin/env python
import argparse
import json
import os
import yaml
from gendiff.generate_diff import generate_diff

parser = argparse.ArgumentParser(description='Compares two configuration '
                                             'files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')

args = parser.parse_args()


def get_format():
    file_extension = os.path.splitext(args.first_file)[1][1:]
    if file_extension == 'yml':
        return yaml
    return json


first_file_path = f"{os.getcwd()}/{args.first_file}"
second_file_path = f"{os.getcwd()}/{args.second_file}"

with open(first_file_path) as first_file_path1:
    with open(second_file_path) as second_file_path1:
        format_file = get_format()
        if format_file == yaml:
            data1 = format_file.load(first_file_path1, Loader=yaml.Loader)
            data2 = format_file.load(second_file_path1, Loader=yaml.Loader)
        else:
            data1 = format_file.load(first_file_path1)
            data2 = format_file.load(second_file_path1)


def main():
    generate_diff(data1, data2)


if __name__ == "main":
    main()
