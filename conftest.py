import allure
import pytest
from register_user import register_new_courier_and_return_login_password
import requests
from data import *
from methods.courier_methods import *
from methods.order_methods import *


@allure.step("Инициализация методов для работы с курьерами")
@pytest.fixture()
def courier_methods():
    return CourierMethods()


@allure.step('Создание рандомного курьера')
@pytest.fixture()
def random_courier(courier_methods):
    courier_data = register_new_courier_and_return_login_password()
    status_code, response_data = courier_methods.post_courier(courier_data)
    courier_data['id'] = response_data.get('id')
    yield status_code, response_data
    courier_methods.delete_courier(courier_data['id'])


@allure.step('Создание рандомного курьера для авторизации и регистрации')
@pytest.fixture()
def courier_data_login():
    courier_methods = CourierMethods()
    data = register_new_courier_and_return_login_password()
    response = requests.post(f"{BASE_URL}{COURIER_LINK}", json=data)
    login_pass = []
    courier_id = None
    if response.status_code == 201:
        login_pass.append(data["login"])
        login_pass.append(data["password"])
        courier_id = response.json().get("id")
    yield {"login": login_pass[0], "password": login_pass[1]}
    courier_methods.delete_courier(courier_id)


@allure.step("Инициализация методов для работы с заказами")
@pytest.fixture()
def order_methods():
    return OrderMethods()
