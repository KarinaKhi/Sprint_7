import pytest
import requests
from register_user import register_new_courier_and_return_login_password
from test_data import BASE_URL, COURIER_LOGIN_LINK


@pytest.fixture
def courier_data():
    data = register_new_courier_and_return_login_password()
    assert data, "Не удалось создать нового курьера"
    return {"login": data[0], "password": data[1]}


class TestCourierLogin:
    def test_courier_login_success(self, courier_data):
        login_data = {"login": courier_data["login"], "password": courier_data["password"]}
        response = requests.post(f'{BASE_URL}{COURIER_LOGIN_LINK}', json=login_data)
        assert response.status_code == 200, "Код ответа при успешной авторизации курьера неверен"
        assert "id" in response.json(), "Ответ не содержит id"

    def test_login_with_incorrect_data(self):
        incorrect_data = {"login": "wrong_login", "password": "wrong_pass"}
        response = requests.post(f'{BASE_URL}{COURIER_LOGIN_LINK}', json=incorrect_data)
        assert response.status_code == 404, "Код ответа при неверных данных авторизации неверен"
        assert "message" in response.json(), "Ответ не содержит сообщение об ошибке"

    def test_login_missing_login_field(self):
        missing_login_data = {"password": "test_pass", "login": ""}
        response = requests.post(f'{BASE_URL}{COURIER_LOGIN_LINK}', json=missing_login_data)
        assert response.status_code == 400, "Код ответа при отсутствии поля login неверен"
        assert "message" in response.json(), "Ответ не содержит сообщение об ошибке"

    def test_login_missing_password_field(self):
        missing_password_data = {"login": "test_login", "password": ""}
        response = requests.post(f'{BASE_URL}{COURIER_LOGIN_LINK}', json=missing_password_data)
        assert response.status_code == 400, "Код ответа при отсутствии поля password неверен"
        assert "message" in response.json(), "Ответ не содержит сообщение об ошибке"

    def test_login_with_incorrect_password(self, courier_data):
        courier_data = register_new_courier_and_return_login_password()
        correct_login = courier_data[0]
        incorrect_password = "wrongpass12345"
        incorrect_password_data = {
            "login": correct_login,
            "password": incorrect_password
        }
        response = requests.post(f'{BASE_URL}{COURIER_LOGIN_LINK}', json=incorrect_password_data)
        assert response.status_code == 404, f"Запрос на создание заказа вернул статус {response.status_code}"
        assert "message" in response.json(), "Ответ не содержит сообщение об ошибке при неверном пароле"
