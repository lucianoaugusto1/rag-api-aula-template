.PHONY: install dev check audit clean-cache

install:
	uv sync

dev:
	uv run uvicorn api.app:app --reload

check:
	uv run python -m py_compile main.py api/app.py core/preprocessing.py

audit:
	uvx pip-audit --path .venv/lib/python3.12/site-packages

clean-cache:
	rm -rf cache/*
