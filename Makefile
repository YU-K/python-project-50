install:
	poetry install

run:
	poetry run gendiff  tests/fixtures/file1_r.json tests/fixtures/file2_r.json
# 	poetry run gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml
# 	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

build:
	poetry build

make test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov

lint:
	poetry run flake8 gendiff
    
publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

