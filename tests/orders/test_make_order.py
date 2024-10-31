import pytest
import json
import requests
from data import BASE_URL, ORDER_LINK, ORDER_DATA_SET_1_BLACK, ORDER_DATA_SET_2_NO_COLOR, \
    ORDER_DATA_SET_3_GREY_AND_BLACK, ORDER_DATA_SET_4_GREY
from methods.order_methods import OrderMethods
from conftest import *
import allure


class TestCreateOrder:

    @allure.title("Проверка создания заказа с параметрами {'order'}")
    @pytest.mark.parametrize("order",
                             [ORDER_DATA_SET_1_BLACK, ORDER_DATA_SET_2_NO_COLOR, ORDER_DATA_SET_3_GREY_AND_BLACK,
                              ORDER_DATA_SET_4_GREY])
    def test_create_order(self, order, order_methods):
        status_code, response_data = order_methods.post_order(order)
        assert status_code == 201 and response_data.get("track") is not None, f"Ошибка при создании заказа"
