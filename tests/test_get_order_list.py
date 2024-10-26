import requests
from test_data import BASE_URL, ORDER_LIST_LINK, courier_id_data_for_get_request


class TestOrderList:

    def test_get_orders_list_response_without_courier_id(self):
        response = requests.get(f'{BASE_URL}{ORDER_LIST_LINK}')
        assert response.status_code == 200, "Код ответа при получении списка заказов неверен"
        assert "orders" in response.json(), "Ответ не содержит orders"
        assert isinstance(response.json()["orders"], list), "Ключ 'orders' должен содержать список заказов"

    def test_get_orders_list_assert_not_empty_response_with_courier_id(self):
        response = requests.get(f'{BASE_URL}{ORDER_LIST_LINK}', params=courier_id_data_for_get_request)
        assert response.status_code == 200, f"Запрос на создание заказа вернул статус {response.status_code}"
        response_data = response.json()

        assert isinstance(response_data, dict), "Ответ должен быть в формате JSON-объекта"
        assert "orders" in response_data, "Ответ не содержит orders"
        assert isinstance(response_data["orders"], list), "Ключ 'orders' должен содержать список заказов"
