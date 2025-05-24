import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru"

def test_get_orders_list():
    response = requests.get(f"{BASE_URL}/api/v1/orders")
    assert response.status_code == 200
    assert "orders" in response.json()
    assert isinstance(response.json()["orders"], list)
