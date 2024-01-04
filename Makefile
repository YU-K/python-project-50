install:
	poetry install

run:
	poetry run gendiff temp/file1.json temp/file2.json -f json

build:
	poetry build


publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

