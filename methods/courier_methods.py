import requests
from data import BASE_URL, COURIER_LINK


class CourierMethods:

    def post_courier(self, courier_data):
        response = requests.post(f"{BASE_URL}{COURIER_LINK}", json=courier_data)
        return response.status_code, response.json()

    def delete_courier(self, courier_id):
        response = requests.delete(f"{BASE_URL}{COURIER_LINK}/{courier_id}")
        return response.status_code

    def post_courier_login(self, login_data):
        response = requests.post(f"{BASE_URL}{COURIER_LINK}/login", json=login_data)
        return response.status_code, response.json()
