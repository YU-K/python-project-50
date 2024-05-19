install:
	poetry install

run:
	poetry run gendiff  -f json tests/fixtures/file1_r.yml tests/fixtures/file2_r.yml

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

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall




