import requests
import allure
from utils.helpers import generate_user_data, register_courier

BASE_URL = "https://qa-scooter.praktikum-services.ru"

@allure.suite("Создание курьера")
class TestCourierCreation:

    @allure.title("Позитивный тест: курьер создается успешно")
    def test_create_courier_success(self):
        user = generate_user_data()
        with allure.step("Отправка запроса на создание курьера"):
            response = register_courier(user)
        assert response.status_code == 201
        assert response.json()["ok"] is True

    @allure.title("Негативный тест: создание дубликата курьера")
    def test_create_duplicate_courier(self):
        user = generate_user_data()
        register_courier(user)
        with allure.step("Повторная отправка запроса с теми же данными"):
            response = register_courier(user)
        assert response.status_code == 409

    @allure.title("Негативный тест: отсутствие пароля")
    def test_create_courier_missing_password(self):
        user = generate_user_data()
        user.pop("password")
        with allure.step("Отправка запроса без пароля"):
            response = register_courier(user)
        assert response.status_code == 400

    @allure.title("Негативный тест: отсутствие логина")
    def test_create_courier_missing_login(self):
        user = generate_user_data()
        user.pop("login")
        with allure.step("Отправка запроса без логина"):
            response = register_courier(user)
        assert response.status_code == 400
