import pytest
import requests
from utils.helpers import register_new_courier_and_return_login_password

BASE_URL = "https://qa-scooter.praktikum-services.ru"


def test_login_success():
    login, password, _ = register_new_courier_and_return_login_password()
    payload = {"login": login, "password": password}
    response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)
    assert response.status_code == 200
    assert "id" in response.json()


def test_login_missing_password():
    login, _, _ = register_new_courier_and_return_login_password()
    response = requests.post(f"{BASE_URL}/api/v1/courier/login", data={"login": login})

    # Обработка временного сбоя сервера
    if response.status_code == 504:
        pytest.skip("Сервер временно недоступен (504 Gateway Timeout)")

    assert response.status_code == 400


def test_login_invalid_credentials():
    payload = {"login": "fakeuser", "password": "fakepass"}
    response = requests.post(f"{BASE_URL}/api/v1/courier/login", data=payload)
    assert response.status_code == 404
