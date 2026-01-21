from abc import ABC, abstractmethod

from app.db.schema import User

class UserServiceInterface(ABC):
    @abstractmethod
    def __init__(self) -> None:
        ...

    @abstractmethod
    def list_users(self) -> list[User]:
        """List all users."""
        ...

    @abstractmethod
    def create_user(self, name: str) -> User:
        """Create a new user with the provided data."""
        ...

    @abstractmethod
    def get_user(self, user_id) -> User | None:
        """Retrieve a user by their unique identifier."""
        ...

    @abstractmethod
    def update_user(self, user_id, name: str) -> User | None:
        """Update the information of an existing user."""
        ...

    @abstractmethod
    def delete_user(self, user_id) -> bool:
        """Delete a user by their unique identifier."""
        ...
