import requests
from utils.helpers import generate_random_string

BASE_URL = "https://qa-scooter.praktikum-services.ru"

def test_create_courier_success():
    payload = {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }
    response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)
    assert response.status_code == 201
    assert response.json()["ok"] is True

def test_create_duplicate_courier():
    login = generate_random_string()
    payload = {
        "login": login,
        "password": "pass123",
        "firstName": "name123"
    }
    requests.post(f"{BASE_URL}/api/v1/courier", data=payload)
    response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)
    assert response.status_code == 409
    assert "Этот логин уже используется" in response.text

def test_create_courier_missing_password():
    payload = {
        "login": generate_random_string(),
        "firstName": "test"
    }
    response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)
    assert response.status_code == 400

def test_create_courier_missing_login():
    payload = {
        "password": generate_random_string(),
        "firstName": "test"
    }
    response = requests.post(f"{BASE_URL}/api/v1/courier", data=payload)
    assert response.status_code == 400
