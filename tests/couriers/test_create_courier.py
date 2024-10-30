import requests
from data import COURIER_LINK, BASE_URL
from conftest import *
from methods.courier_methods import CourierMethods


class TestCourierCreation:

    def test_create_courier_successfully(self, courier_methods, random_courier):
        status_code, response_data = random_courier
        assert status_code == 201 and response_data == {"ok": True}, "Ошибка при создании курьера"

    def test_create_duplicate_courier(self, courier_methods, courier_data_login):
        courier_methods.post_courier(courier_data_login)
        status_code, response_data = courier_methods.post_courier(courier_data_login)
        assert status_code == 409 and "message" in response_data, "Ошибка при проверке дублирования курьера"

    @pytest.mark.parametrize("field", ["login", "password"])
    def test_create_courier_missing_required_fields(self, courier_methods, courier_data_login, field):
        courier_data_login[field] = ""
        status_code, response_data = courier_methods.post_courier(courier_data_login)
        assert status_code == 400 and "message" in response_data, "Ошибка при проверке обязательных полей"

    def test_create_courier_with_existing_login(self, courier_methods, courier_data_login):
        courier_methods.post_courier(courier_data_login)
        status_code, response_data = courier_methods.post_courier(courier_data_login)
        assert status_code == 409 and "message" in response_data, "Ошибка при проверке логина"
