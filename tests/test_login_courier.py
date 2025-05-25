import requests
import allure
from utils.helpers import generate_user_data, register_courier

BASE_URL = "https://qa-scooter.praktikum-services.ru"

@allure.suite("Логин курьера")
class TestCourierLogin:

    @allure.title("Позитивный тест: логин успешен")
    def test_login_success(self):
        user = generate_user_data()
        register_courier(user)
        with allure.step("Попытка логина с валидными данными"):
            response = requests.post(f"{BASE_URL}/api/v1/courier/login", data={
                "login": user["login"],
                "password": user["password"]
            })
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Негативный тест: отсутствие пароля")
    def test_login_missing_password(self):
        user = generate_user_data()
        register_courier(user)
        with allure.step("Попытка логина без пароля"):
            response = requests.post(f"{BASE_URL}/api/v1/courier/login", data={"login": user["login"]})
        assert response.status_code == 400

    @allure.title("Негативный тест: несуществующий пользователь")
    def test_login_invalid_credentials(self):
        with allure.step("Попытка логина с фейковыми данными"):
            response = requests.post(f"{BASE_URL}/api/v1/courier/login", data={
                "login": "nonexistent",
                "password": "wrongpass"
            })
        assert response.status_code == 404
