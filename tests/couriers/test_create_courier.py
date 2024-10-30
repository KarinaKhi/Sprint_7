import requests

from data import COURIER_LINK, BASE_URL
from conftest import *
from methods.courier_methods import CourierMethods

#
# class Test1CourierCreation:
#
#     def test_create_courier_successfully(self, random_courier):
#         response = requests.post(f"{BASE_URL}{COURIER_LINK}", json=random_courier)
#         response_data = response.json()
#
#         assert response.status_code == 201, f"Ожидался статус 201, получено {response.status_code}"
#         assert response_data == {"ok": True}, "Ответ не содержит {'ok': true}"


class TestCourierCreation:

    # def test_create_courier_successfully(self, courier_methods, random_courier):
    #     status_code, response_data = courier_methods.post_courier(random_courier)
    #     assert status_code == 201 and response_data == {"ok": True}, "Ошибка при создании курьера"

    def test_create_duplicate_courier(self, courier_methods, random_courier):
        courier_methods.post_courier(random_courier)
        status_code, response_data = courier_methods.post_courier(random_courier)
        assert status_code == 409 and "message" in response_data, "Ошибка при проверке дублирования курьера"

    @pytest.mark.parametrize("field", ["login", "password"])
    def test_create_courier_missing_required_fields(self, courier_methods, random_courier, field):
        random_courier[field] = ""
        status_code, response_data = courier_methods.post_courier(random_courier)
        assert status_code == 400 and "message" in response_data, "Ошибка при проверке обязательных полей"

    def test_create_courier_with_existing_login(self, courier_methods, random_courier):
        courier_methods.post_courier(random_courier)
        status_code, response_data = courier_methods.post_courier(random_courier)
        assert status_code == 409 and "message" in response_data, "Ошибка при проверке логина"
