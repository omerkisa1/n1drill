.PHONY: install lint fmt type test cov check clean

install:
	uv sync --all-groups

lint:
	uv run ruff check .

fmt:
	uv run ruff format .

type:
	uv run mypy src

test:
	uv run pytest

cov:
	uv run pytest --cov

check: lint type test
	@echo "all checks passed"

clean:
	rm -rf .venv .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage dist
	find . -type d -name __pycache__ -exec rm -rf {} +
