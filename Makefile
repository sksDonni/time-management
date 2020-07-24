.PHONY:init
init:
	pipenv shell --python 3.8

.PHONY: install
install:
	pipenv install

.PHONY: format
format:
	black .

.PHONY: lint
lint:
	flake8 . --ignore=E501

.PHONY: clean
clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +

.PHONY: test
test:
	python -m unittest discover . "*_test.py"

.PHONY: run
run:
	python3 main.py

.PHONY: remove
remove:
	pipenv --rm