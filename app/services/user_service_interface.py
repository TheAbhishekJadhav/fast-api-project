from abc import ABC, abstractmethod

from app.db.schema import User

class UserServiceInterface(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def list_users(self) -> list[User]:
        """List all users."""
        pass

    @abstractmethod
    def create_user(self, name: str) -> User:
        """Create a new user with the provided data."""
        pass

    @abstractmethod
    def get_user(self, user_id) -> User | None:
        """Retrieve a user by their unique identifier."""
        pass

    @abstractmethod
    def update_user(self, user_id, name: str) -> User | None:
        """Update the information of an existing user."""
        pass

    @abstractmethod
    def delete_user(self, user_id) -> bool:
        """Delete a user by their unique identifier."""
        pass
