from fastapi.testclient import TestClient
from app.main import app
from app.services.user_service import UserService
from tests.test_db import TestingSessionLocal

# Setup test client
client = TestClient(app)

# Dependency override to use test database session
def override_get_user_service():
    session = TestingSessionLocal()  # Assume TestingSessionLocal is a test database session
    yield UserService(session=session)

app.dependency_overrides[UserService] = override_get_user_service

def test_create_user_and_get_user():
    # Test user creation
    response = client.post("/api/v1/users", json={"name": "Test User"})
    assert response.status_code == 200
    created_user = response.json()
    assert created_user["name"] == "Test User"
    assert "id" in created_user

    # Test getting the created user
    get_response = client.get(f"/api/v1/users/{created_user['id']}")
    assert get_response.status_code == 200
    fetched_user = get_response.json()
    assert fetched_user == created_user
    