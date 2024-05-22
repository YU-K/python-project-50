#!/usr/bin/env python
import os
from gendiff import generate_diff
from gendiff.gendiff import read_file
import pytest


def get_fixture_path(filename: str) -> str:
    current_dir = os.getcwd()
    return os.path.join(current_dir, "tests/fixtures", filename)


file_path_json1 = get_fixture_path("file1_r.json")
file_path_json2 = get_fixture_path("file2_r.json")
file_path_yml1 = get_fixture_path("file1_r.yml")
file_path_yml2 = get_fixture_path("file2_r.yml")
json_output = read_file(get_fixture_path("json.txt"))
stylish_output = read_file(get_fixture_path("stylish.txt"))
plain_output = read_file(get_fixture_path("plain.txt"))


testdata = [(file_path_json1, file_path_json2, 'stylish', stylish_output),
            (file_path_yml1, file_path_yml2, 'stylish', stylish_output),
            (file_path_json1, file_path_json2, 'json', json_output),
            (file_path_yml1, file_path_yml2, 'json',  json_output),
            (file_path_yml1, file_path_yml2, 'plain', plain_output),]


@pytest.mark.parametrize("file1, file2, format_name, expected", testdata)
def test_generate_diff(file1, file2, format_name, expected):
    diff = generate_diff(file1, file2, format_name)
    assert diff == expected.strip()
