run:
	uv run uvicorn app.main:app --reload

test:
	uv run pytest -v --cov=app tests/
