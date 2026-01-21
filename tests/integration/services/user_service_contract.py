from app.services.user_service_interface import UserServiceInterface

class UserServiceTestContract:
    """
    Contract for User Service integration tests.
    """
    def __init__(self, service: UserServiceInterface) -> None:
        self.service = service

    def test_list_users(self):
        # Create multiple users
        user1 = self.service.create_user("Alice")
        user2 = self.service.create_user("Bob")
        user3 = self.service.create_user("Charlie")

        # List all users
        users = self.service.list_users()

        assert len(users) == 3
        assert users == [user1, user2, user3]
    
    def test_get_user(self):
        # Create a user
        user = self.service.create_user("David")

        # Retrieve the user by ID
        fetched_user = self.service.get_user(user.id)

        assert fetched_user == user

        # Try to get a non-existing user
        non_existing_user = self.service.get_user(9999)
        assert non_existing_user is None

    def test_update_user(self):
        # Create a user
        user = self.service.create_user("Eve")
        
        # Update the user's name
        updated_user = self.service.update_user(user.id, "Eve Updated")

        assert updated_user is not None
        assert updated_user.name == "Eve Updated"
        assert updated_user.id == user.id

        # Try to update a non-existing user
        non_existing_update = self.service.update_user(9999, "No One")
        assert non_existing_update is None

    def test_delete_user(self):
        # Create a user
        user = self.service.create_user("Frank")

        # Delete the user
        delete_result = self.service.delete_user(user.id)
        assert delete_result is True

        # Verify the user is deleted
        fetched_user = self.service.get_user(user.id)
        assert fetched_user is None

        # Try to delete a non-existing user
        non_existing_delete = self.service.delete_user(9999)
        assert non_existing_delete is False


