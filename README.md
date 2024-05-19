## Hexlet tests and linter status:
[![Actions Status](https://github.com/YU-K/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/YU-K/python-project-50/actions)

## Gendiff app CI
[![Actions Status](https://github.com/YU-K/python-project-50/actions/workflows/python-app.yml/badge.svg)](https://github.com/YU-K/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/68596315200ecc1958fc/maintainability)](https://codeclimate.com/github/YU-K/python-project-50/maintainability)   [![Test Coverage](https://api.codeclimate.com/v1/badges/68596315200ecc1958fc/test_coverage)](https://codeclimate.com/github/YU-K/python-project-50/test_coverage)

## Description

"gendiff" is a command line utility that compares two files line by line and shows a difference.\
Supports plain, recursive, json output formats. 

## Installation

```
>> Make install
```

## Usage

```
gendiff [-h] [-f FORMAT] first_file second_file

options:
    -h, --help                    shows this help message and exit
    -f FORMAT, --format FORMAT    set format of output (default: stylish)
```
## Examples


#### Compare two json files
[![asciicast](https://asciinema.org/a/opJlsgOBM8cwyZ2shqRLoZUmF.svg)](https://asciinema.org/a/opJlsgOBM8cwyZ2shqRLoZUmF)

#### Compare two yaml files
[![asciicast](https://asciinema.org/a/RmFZhdN7F2yZIJbI7dONUCDno.svg)](https://asciinema.org/a/RmFZhdN7F2yZIJbI7dONUCDno)

#### Recursive comparison of two files
[![asciicast](https://asciinema.org/a/QCkMH4AXCoXLj3BV1Xj3rYpPe.svg)](https://asciinema.org/a/QCkMH4AXCoXLj3BV1Xj3rYpPe)

#### Recursive comparison of two files in plain, tree, json formats
[![asciicast](https://asciinema.org/a/6CIWNmwwzmvBURqhFWL2UbD1d.svg)](https://asciinema.org/a/6CIWNmwwzmvBURqhFWL2UbD1d)