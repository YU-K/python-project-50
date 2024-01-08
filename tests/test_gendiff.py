#!/usr/bin/env python
import os
import json
import yaml
from gendiff.generate_diff import generate_diff


first_file_path = f"{os.getcwd()}/tests/fixtures/file1.json"
second_file_path = f"{os.getcwd()}/tests/fixtures/file2.json"
result = f"{os.getcwd()}/tests/fixtures/output.txt"

first_file_path_yml = f"{os.getcwd()}/tests/fixtures/file1.yml"
second_file_path_yml = f"{os.getcwd()}/tests/fixtures/file2.yml"


data1 = json.load(open(first_file_path))
data2 = json.load(open(second_file_path))
content_output = open(result).read()

data1_yml = yaml.load(open(first_file_path_yml), Loader=yaml.Loader)
data2_yml = yaml.load(open(second_file_path_yml), Loader=yaml.Loader)


# @pytest.mark.parametrize("file1, file2, expected", [(first_file_path, second_file_path, result)])
def test_generate_diff():
    assert generate_diff(data1_yml, data2_yml) == content_output.strip()
    # assert generate_diff(data1, data2) == content_output.strip()
