# Template Service

FastAPI microservice template: package-by-feature at the top level, layered
inside each feature, Postgres-backed, Scalar API docs.

# How to Run

## Create Virtual Environent

```bash
python -m venv ".venv"
```

## Setup + Install Dependencies

```bash
cd app
pip install -e . --break-system-packages
```

## Run (development)

```bash
fastapi dev template_service/main.py
```

## Run (production-style)

```bash
fastapi run template_service/main.py
```

## Docs

Interactive Scalar API docs, once running:

```
http://127.0.0.1:8000/docs
```

# Testing

## Run all tests

```bash
pytest -v
```

## Run a folder (or single file)

```bash
pytest tests/path/to/file/or/folder
```

## Run until failure

```bash
pytest -x
```

## Discover all tests to run

```bash
pytest --collect-only
```
