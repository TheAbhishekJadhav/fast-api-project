run:
	uv run uvicorn app.main:app --reload

test:
	uv run pytest -v --cov=app tests/

test-unit:
	uv run pytest -v --cov=app tests/unit

test-integration:
	uv run pytest -v --cov=app tests/integration
