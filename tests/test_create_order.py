import pytest
import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru"

order_url = f"{BASE_URL}/api/v1/orders"

@pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
def test_create_order_with_colors(color):
    payload = {
        "firstName": "John",
        "lastName": "Doe",
        "address": "123 Main St",
        "metroStation": 4,
        "phone": "+7 999 999 99 99",
        "rentTime": 5,
        "deliveryDate": "2025-05-21",
        "comment": "Test order",
        "color": color
    }
    response = requests.post(order_url, json=payload)
    assert response.status_code == 201
    assert "track" in response.json()
