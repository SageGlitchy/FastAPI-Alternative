# Contributing to FastAPI

Thank you for your interest in contributing to FastAPI! 🎉

For the full, detailed contributing guide, please visit the official documentation:
**[https://fastapi.tiangolo.com/contributing/](https://fastapi.tiangolo.com/contributing/)**

This document provides a quick-start reference for local development.

## Prerequisites

- **Python 3.10+**
- **[uv](https://docs.astral.sh/uv/)** — fast Python package manager

## Setup

Clone the repository and install all dependencies:

```bash
git clone https://github.com/fastapi/fastapi.git
cd fastapi
uv sync
```

This installs all development, test, and documentation dependencies.

## Running Tests

Run the full test suite:

```bash
uv run pytest tests/
```

Run tests with coverage:

```bash
uv run bash scripts/test-cov.sh
```

Run a specific test file:

```bash
uv run pytest tests/test_tutorial/test_security/ -v
```

## Type Checking

Run mypy against the FastAPI source:

```bash
uv run mypy fastapi
```

## Linting

Run the ruff linter:

```bash
uv run ruff check .
```

Auto-fix linting issues:

```bash
uv run ruff check . --fix
```

## Formatting

Format code with ruff:

```bash
uv run ruff format .
```

## Pre-commit Hooks

The project uses pre-commit hooks via [prek](https://github.com/tiangolo/prek). These run automatically in CI through the [pre-commit.yml](.github/workflows/pre-commit.yml) workflow.

## Pull Request Guidelines

1. **Fork** the repository and create a feature branch from `master`.
2. **Write tests** for any new functionality or bug fixes.
3. **Run the full test suite** locally before submitting:
   ```bash
   uv run pytest tests/
   uv run mypy fastapi
   uv run ruff check .
   ```
4. **Keep commits focused** — one logical change per commit.
5. **Update documentation** if your change affects user-facing behavior.

### CI Checks

Your PR must pass all CI checks before merging:

- **[test.yml](.github/workflows/test.yml)** — runs the full test suite across multiple Python versions and operating systems, plus lint and type checking.
- **[pre-commit.yml](.github/workflows/pre-commit.yml)** — runs formatting and linting hooks.

## Docker

You can also run the project using Docker:

```bash
docker compose up
```

This starts the FastAPI demo app at [http://localhost:8000](http://localhost:8000) with a PostgreSQL database.

## Questions?

- Open a [GitHub Discussion](https://github.com/fastapi/fastapi/discussions)
- Check the [documentation](https://fastapi.tiangolo.com/)
