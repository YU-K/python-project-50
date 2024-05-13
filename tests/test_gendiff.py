#!/usr/bin/env python
import os
import json
import yaml
from gendiff.generate_diff import generate_diff
from gendiff.formatters.plain import plain
import pytest


def get_fixture_path(filename: str) -> str:
    current_dir = os.getcwd()
    return os.path.join(current_dir, "tests/fixtures", filename)


data1 = json.load(open(get_fixture_path("file1.json")))
data2 = json.load(open(get_fixture_path("file2.json")))
data1_r = json.load(open(get_fixture_path("file1_r.json")))
data2_r = json.load(open(get_fixture_path("file2_r.json")))
data1_yml = yaml.load(open(get_fixture_path("file1.yml")), Loader=yaml.Loader)
data2_yml = yaml.load(open(get_fixture_path("file2.yml")), Loader=yaml.Loader)
expected = open(get_fixture_path("output.txt")).read()
expected_recur = open(get_fixture_path("output_r.txt")).read()
expected_plain = open(get_fixture_path("output_plain.txt")).read()

# TODO: добавить возможность подставлять различные файлы в pytest
# @pytest.mark.parametrize("file1, file2, expected", [(first_file_path, second_file_path, result)])

testdata = [
            # (data1, data2, expected),
            # (data1_yml, data2_yml, expected),
            # (data1_r, data2_r, expected_recur),
            (data1_r, data2_r, expected_plain),
]


@pytest.mark.parametrize("file1, file2, expected", testdata)
def test_generate_diff(file1, file2, expected):
    diff = generate_diff(file1, file2, plain)
    assert diff == expected.strip()
