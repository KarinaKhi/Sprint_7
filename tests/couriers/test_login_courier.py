from conftest import *
import allure


class TestCourierLogin:

    @allure.title('Проверка авторизации курьера с корректными данными')
    def test_courier_login_success(self, courier_methods, courier_data_login):
        status_code, response_data = courier_methods.post_courier_login(courier_data_login)
        assert status_code == 200 and "id" in response_data, "Ошибка при авторизации курьера"

    @allure.title('Проверка корректной ошибки при попытки авторизации с полностью некорректными данными в обоих полях')
    def test_login_with_incorrect_data(self, courier_methods):
        incorrect_data = {"login": "wrong_login", "password": "wrong_pass"}
        status_code, response_data = courier_methods.post_courier_login(incorrect_data)
        assert (status_code == 404 and response_data["message"] == "Учетная запись не найдена"),\
            f"Получили статус {status_code} и сообщение '{response_data.get('message', 'Нет сообщения')}'"

    @allure.title('Проверка корректной ошибки при попытки авторизации без поля логин')
    def test_login_missing_login_field(self, courier_methods):
        missing_login_data = {"password": "test_pass", "login": ""}
        status_code, response_data = courier_methods.post_courier_login(missing_login_data)
        assert (status_code == 400 and response_data["message"] == "Недостаточно данных для входа"),\
            f"Получили статус {status_code} и сообщение '{response_data.get('message', 'Нет сообщения')}'"

    @allure.title('Проверка корректной ошибки при попытки авторизации без поля пароль')
    def test_login_missing_password_field(self, courier_methods):
        missing_password_data = {"login": "test_login", "password": ""}
        status_code, response_data = courier_methods.post_courier_login(missing_password_data)
        assert (status_code == 400 and response_data["message"] == "Недостаточно данных для входа"), \
            f"Получили статус {status_code} и сообщение '{response_data.get('message', 'Нет сообщения')}'"

    @allure.title('Проверка корректной ошибки при попытки авторизации с некорректным паролем')
    def test_login_with_incorrect_password(self, courier_methods, courier_data_login):
        correct_login = courier_data_login["login"]
        incorrect_password_data = {"login": correct_login, "password": "wrongpass12345"}
        status_code, response_data = courier_methods.post_courier_login(incorrect_password_data)
        assert (status_code == 404 and response_data["message"] == "Учетная запись не найдена"), \
            f"Получили статус {status_code} и сообщение '{response_data.get('message', 'Нет сообщения')}'"
