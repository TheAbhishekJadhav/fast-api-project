# FastAPI User Management Project

A simple FastAPI application for managing users with CRUD operations, built with a focus on clean architecture, dependency injection, and comprehensive testing.

## Features

- **CRUD Operations**: Create, read, update, and delete users.
- **Database Integration**: Uses SQLAlchemy with SQLite for data persistence.
- **API Documentation**: Auto-generated Swagger UI at `/docs`.
- **Testing Strategy**: Layered testing with unit, integration, and contract tests for high reliability.
- **Clean Architecture**: Separation of concerns with services, interfaces, and dependency injection.

## Installation and Setup

1. **Clone the repository**:
   ```shell
   git clone <repository-url>
   cd fast-api-project
   ```

2. **Install dependencies**:
   ```shell
   uv sync
   ```

3. **Set up the database** (if needed):
   The app uses SQLite, and tables are created automatically on startup.

## Starting the Server

```shell
uv run uvicorn app.main:app --reload
```
or
```shell
make run
```

The server will run at `http://localhost:8000`. Visit `/docs` for interactive API documentation.

## API Usage

Here’s a set of simple curl examples to interact with the API:

### 1️⃣ Create a User
```shell
curl -X POST "http://localhost:8000/api/v1/users" \
-H "Content-Type: application/json" \
-d '{"name": "Ada Lovelace"}'
```

### 2️⃣ Get All Users
```shell
curl -X GET "http://localhost:8000/api/v1/users"
```

### 3️⃣ Get a User by ID
(Replace `1` with the actual ID from the create response)
```shell
curl -X GET "http://localhost:8000/api/v1/users/1"
```

### 4️⃣ Update a User
```shell
curl -X PUT "http://localhost:8000/api/v1/users/1" \
-H "Content-Type: application/json" \
-d '{"name": "Grace Hopper"}'
```

### 5️⃣ Delete a User
```shell
curl -X DELETE "http://localhost:8000/api/v1/users/1"
```

## Testing

This project follows a robust testing strategy with multiple layers. For detailed information on our testing design, benefits, and standards, see [tests/README.md](tests/README.md).

### Run All Tests
```shell
uv run pytest -v
```

### Run Tests with Coverage
```shell
uv run pytest -v --cov=app
```
or
```shell
make test
```

### Test Structure
- **Unit Tests**: Isolated tests using fake services (`tests/unit/`).
- **Integration Tests**: End-to-end tests with real database (`tests/integration/`).
- **Contract Tests**: Behavioral verification across service implementations.

## Project Structure

```
fast-api-project/
├── app/
│   ├── api/v1/          # API routes
│   ├── core/            # Configuration and logging
│   ├── db/              # Database schema
│   ├── models/          # Pydantic models
│   ├── services/        # Business logic and interfaces
│   └── main.py          # App entry point
├── tests/               # Test suite
│   ├── unit/            # Unit tests
│   ├── integration/     # Integration tests
│   └── README.md        # Testing documentation
├── pyproject.toml       # Project dependencies
├── makefile             # Build scripts
└── README.md            # This file
```
