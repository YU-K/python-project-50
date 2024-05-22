#!/usr/bin/env python
import argparse
from gendiff import generate_diff


arg_parser = argparse.ArgumentParser(
    description='Compares two configuration '
                'files and shows a difference.')
arg_parser.add_argument('first_file')
arg_parser.add_argument('second_file')
arg_parser.add_argument('-f', '--format',
                        default='stylish',
                        help='set format of output (default: stylish)')

args = arg_parser.parse_args()

file_path1 = args.first_file
file_path2 = args.second_file
format_name = args.format


def main():
    diff = generate_diff(file_path1, file_path2, format_name)
    print(diff)


if __name__ == "main":
    main()
