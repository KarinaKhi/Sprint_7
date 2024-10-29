import requests

from test_data import COURIER_CREATION_LINK, BASE_URL
from conftest import *


class TestCourierCreation:

    def test_create_courier_successfully(self, random_courier):
        response = requests.post(f"{BASE_URL}{COURIER_CREATION_LINK}", json=random_courier)
        response_data = response.json()

        assert response.status_code == 201, f"Ожидался статус 201, получено {response.status_code}"
        assert response_data == {"ok": True}, "Ответ не содержит {'ok': true}"

    def test_create_duplicate_courier(self, random_courier):
        requests.post(f"{BASE_URL}{COURIER_CREATION_LINK}", json=random_courier)
        response = requests.post(f"{BASE_URL}{COURIER_CREATION_LINK}", json=random_courier)
        response_data = response.json()
        assert response.status_code == 409, f"Ожидался статус 409, получено {response.status_code}"
        assert "message" in response.json(), "Ответ не содержит сообщение об ошибке"

    @pytest.mark.parametrize("field", ["login", "password"])
    def test_create_courier_missing_required_fields(self, random_courier, field):
        random_courier[field] = ""
        response = requests.post(f"{BASE_URL}{COURIER_CREATION_LINK}", json=random_courier)
        response_data = response.json()
        assert response.status_code == 400, f"Ожидался статус 400, получено {response.status_code}"
        assert "message" in response.json(), "Ответ не содержит сообщение об ошибке"

    def test_create_courier_with_existing_login(self, random_courier):
        requests.post(f"{BASE_URL}{COURIER_CREATION_LINK}", json=random_courier)
        response = requests.post(f"{BASE_URL}{COURIER_CREATION_LINK}", json=random_courier)
        response_data = response.json()
        assert response.status_code == 409, f"Ожидался статус 409, получено {response.status_code}"
        assert "message" in response.json(), "Ответ не содержит сообщение об ошибке"
