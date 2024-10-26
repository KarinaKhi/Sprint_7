import pytest
from register_user import register_new_courier_and_return_login_password


@pytest.fixture(scope="function")
def create_courier():
    courier_data = register_new_courier_and_return_login_password()
    yield courier_data

