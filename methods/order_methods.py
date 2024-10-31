import allure
import requests
from data import BASE_URL, ORDER_LINK


class OrderMethods:
    @allure.step("Создание заказа")
    def post_order(self, order):
        response = requests.post(f'{BASE_URL}{ORDER_LINK}', json=order)
        return response.status_code, response.json()

    @allure.step("Получение списка заказов")
    def get_orders(self):
        response = requests.get(f'{BASE_URL}{ORDER_LINK}')
        return response.status_code, response.json()


