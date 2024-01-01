.PHONY: help install dev format lint test
SHELL := /bin/bash # Use bash syntax

PYTEST_CMD=pytest tests -vv

# dev aliases format and lint
RUFF=ruff app tests
FORMAT=ruff format app tests
MYPY=mypy app tests

help: ## Show this help.
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install dependencies (including dev deps) inside current venv.
	pip install -U pip
	pip install poetry==1.7.1
	poetry install

dev:  ## Run the service.
	uvicorn app.main:app --host 0.0.0.0 --port 5003 --reload

format:  ## Reformat project code.
	${RUFF} --fix
	${FORMAT}

lint:  ## Lint project code.
	${RUFF}
	${FORMAT} --check
	${MYPY}

test:  ## Run test suite and generate coverage as html format + stdout.
	$(PYTEST_CMD) --cov=fasthtmx --cov-report=html:htmlcov --cov-report=term-missing -vv
