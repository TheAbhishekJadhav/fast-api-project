from tests.integration.services.user_service_contract import UserServiceTestContract
from tests.unit.services.fake_user_service import FakeUserService

service = FakeUserService()

test_contract = UserServiceTestContract(service)

def test_list_users():
    test_contract.test_list_users()

def test_get_user():
    test_contract.test_get_user()

def test_update_user():
    test_contract.test_update_user()

def test_delete_user():
    test_contract.test_delete_user()
