from app.db.schema import User
from app.services.user_service_interface import UserServiceInterface

class FakeUserService(UserServiceInterface):
    def __init__(self) -> None:
        self._users = {}
        self._next_id = 1

    def list_users(self) -> list[User]:
        return list(self._users.values())

    def create_user(self, name: str) -> User:
        user = User(id=self._next_id, name=name)
        self._users[self._next_id] = user
        self._next_id += 1
        return user

    def get_user(self, user_id: int) -> User | None:
        return self._users.get(user_id)

    def update_user(self, user_id: int, name: str) -> User | None:
        if user_id in self._users:
            self._users[user_id].name = name
            return self._users[user_id]
        return None

    def delete_user(self, user_id: int):
        if user_id in self._users:
            del self._users[user_id]
            return True
        return False