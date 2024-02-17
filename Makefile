.PHONY: config

config:
	@poetry config virtualenvs.in-project true --local
	@make prod
prod:
	@poetry install --no-interaction --without dev
	@poetry shell
dev:
	@make install
	@make format
	@make lint
	@make sec
	@make test
install:
	@poetry install --no-interaction
	@poetry shell
format:
	@isort .
	@blue .
lint:
	@isort . --check
	@blue . --check
sec:
	@safety check
test:
	@pytest -v oas_cli tests --cov --cov-fail-under 90 --cov-report html