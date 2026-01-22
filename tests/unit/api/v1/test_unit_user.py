from fastapi.testclient import TestClient
from app.main import app
from app.services.user_service_interface import UserServiceInterface
from tests.unit.services.fake_user_service import FakeUserService

# Setup test client
client = TestClient(app)

# Dependency override to use FakeUserService
def override_get_user_service():
    yield FakeUserService()

app.dependency_overrides[UserServiceInterface] = override_get_user_service

# Sociable unit tests for user API endpoints
def test_create_user():
    response = client.post("/api/v1/users", json={"name": "Unit Test User"})
    assert response.status_code == 200
    created_user = response.json()
    assert created_user["name"] == "Unit Test User"
    assert "id" in created_user

    # Test getting the created user
    get_response = client.get(f"/api/v1/users/{created_user['id']}")
    assert get_response.status_code == 200
    fetched_user = get_response.json()
    assert fetched_user == created_user
    
def test_update_user():
    # Update non-existing user
    response = client.put("/api/v1/users/9999", json={"name": "New Name"})
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

    # Create a user to update
    response = client.post("/api/v1/users", json={"name": "Old Name"})
    assert response.status_code == 200
    user = response.json()

    # Update the user's name
    update_response = client.put(f"/api/v1/users/{user['id']}", json={"name": "New Name"})
    assert update_response.status_code == 200
    updated_user = update_response.json()
    assert updated_user["name"] == "New Name"

    # Verify the update
    get_response = client.get(f"/api/v1/users/{user['id']}")
    assert get_response.status_code == 200
    fetched_user = get_response.json()
    assert fetched_user["name"] == "New Name"

def test_delete_user():
    # Delete non-existing user
    response = client.delete("/api/v1/users/9999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
    
    # Create a user to delete
    response = client.post("/api/v1/users", json={"name": "To Be Deleted"})
    assert response.status_code == 200
    user = response.json()

    # Delete the user
    delete_response = client.delete(f"/api/v1/users/{user['id']}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"Success": True}

    # Verify the user is deleted
    get_response = client.get(f"/api/v1/users/{user['id']}")
    assert get_response.status_code == 404
    assert get_response.json() == {"detail": "User not found"}

def test_list_users():
    # Create multiple users
    client.post("/api/v1/users", json={"name": "User 1"})
    client.post("/api/v1/users", json={"name": "User 2"})

    # List users
    list_response = client.get("/api/v1/users")
    assert list_response.status_code == 200
    users = list_response.json()
    assert len(users) >= 2  # At least the two we just created
    names = [user["name"] for user in users]
    assert "User 1" in names
    assert "User 2" in names
