import allure
import requests
from data import BASE_URL, ORDER_LINK, courier_id_data_for_get_request
from conftest import *
from methods.order_methods import *


class TestOrderList:

    @allure.title('Проверка получения списка всех заказов')
    def test_get_orders_list_response_without_courier_id(self, order_methods):
        status_code, response_data = order_methods.get_orders()
        assert status_code == 200 and "orders" in response_data, f"Ошибка при получении заказов"

    @allure.title('Проверка получения списка заказов одного курьера')
    def test_get_orders_list_assert_not_empty_response_with_courier_id(self):
        response = requests.get(f'{BASE_URL}{ORDER_LINK}', params=courier_id_data_for_get_request)
        response_data = response.json()
        expected_fields = [
            "id", "courierId", "firstName", "lastName", "address", "metroStation",
            "phone", "rentTime", "deliveryDate", "track", "color",
            "comment", "createdAt", "updatedAt", "status"
        ]
        assert response.status_code == 200 and "orders" in response_data, "Ошибка при получении заказов"
        for order in response_data["orders"]:
            assert all(
                field in order and order[field] not in [None, "", []]
                for field in expected_fields
            ), f"Некоторые поля в заказе {order.get('id')} отсутствуют или пусты"