import requests
import allure

BASE_URL = "https://qa-scooter.praktikum-services.ru"

@allure.suite("Список заказов")
class TestGetOrders:

    @allure.title("Позитивный тест: получение списка заказов")
    def test_get_orders_list(self):
        with allure.step("Отправка GET запроса для получения списка заказов"):
            response = requests.get(f"{BASE_URL}/api/v1/orders")
        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
