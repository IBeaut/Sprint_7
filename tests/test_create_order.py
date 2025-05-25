import pytest
import requests
import allure

BASE_URL = "https://qa-scooter.praktikum-services.ru"

@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.title("Проверка создания заказа с разными цветами")
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_with_colors(self, color):
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
        with allure.step(f"Создание заказа с цветами: {color}"):
            response = requests.post(f"{BASE_URL}/api/v1/orders", json=payload)
        assert response.status_code == 201
        assert "track" in response.json()
