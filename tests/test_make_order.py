import pytest
import json
import requests
from test_data import BASE_URL, ORDER_LIST_LINK, ORDER_DATA_SET_1_BLACK, ORDER_DATA_SET_2_NO_COLOR, \
    ORDER_DATA_SET_3_GREY_AND_BLACK, ORDER_DATA_SET_4_GREY


@pytest.fixture(scope="module")
def load_order_data():
    with open("order_data.json") as f:
        return json.load(f)


class TestCreateOrder:

    @pytest.mark.parametrize("order",
                             [ORDER_DATA_SET_1_BLACK, ORDER_DATA_SET_2_NO_COLOR, ORDER_DATA_SET_3_GREY_AND_BLACK,
                              ORDER_DATA_SET_4_GREY])
    def test_create_order(self, order):
        response = requests.post(f"{BASE_URL}{ORDER_LIST_LINK}", json=order)
        response_data = response.json()
        assert response.status_code == 201, f"Запрос на создание заказа вернул статус {response.status_code}"
        assert "track" in response_data, f"Ответ не содержит track при цветах {order['color']}"
        assert response_data["track"] is not None, "Значение track не должно быть пустым"
