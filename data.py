BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'
COURIER_LINK = "/courier"
ORDER_LINK = "/orders"

courier_id_data_for_get_request = {
    "courierId": "406655"
}

ORDER_DATA_SET_1_BLACK = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-11-06",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK"],
    "description": "Заказ с цветом BLACK"
}

ORDER_DATA_SET_2_NO_COLOR = {
    "firstName": "Sakura",
    "lastName": "Haruno",
    "address": "Konoha, 77 apt.",
    "metroStation": 2,
    "phone": "+7 800 355 35 36",
    "rentTime": 3,
    "deliveryDate": "2024-11-06",
    "comment": "Need it fast",
    "color": [],
    "description": "Заказ без указания цвета"
}

ORDER_DATA_SET_3_GREY_AND_BLACK= {
    "firstName": "Sakura",
    "lastName": "Haruno",
    "address": "Konoha, 77 apt.",
    "metroStation": 2,
    "phone": "+7 800 355 35 36",
    "rentTime": 3,
    "deliveryDate": "2024-11-06",
    "comment": "Need it fast",
    "color": ["BLACK", "GRAY"],
    "description": "Оба цвета: BLACK и GREY"
}
ORDER_DATA_SET_4_GREY= {
    "firstName": "Sakura",
    "lastName": "Haruno",
    "address": "Konoha, 77 apt.",
    "metroStation": 2,
    "phone": "+7 800 355 35 36",
    "rentTime": 3,
    "deliveryDate": "2024-11-06",
    "comment": "Need it fast",
    "color": ["BLACK", "GREY"],
    "description": "Заказ с цветом GREY"
}
