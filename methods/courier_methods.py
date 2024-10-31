import requests
from data import BASE_URL, COURIER_LINK
import allure

class CourierMethods:

    @allure.step("Создание курьера")
    def post_courier(self, courier_data):
        response = requests.post(f"{BASE_URL}{COURIER_LINK}", json=courier_data)
        return response.status_code, response.json()

    @allure.step("Удаление курьера")
    def delete_courier(self, courier_id):
        response = requests.delete(f"{BASE_URL}{COURIER_LINK}/{courier_id}")
        return response.status_code

    @allure.step("Авторизация курьера")
    def post_courier_login(self, login_data):
        response = requests.post(f"{BASE_URL}{COURIER_LINK}/login", json=login_data)
        return response.status_code, response.json()
