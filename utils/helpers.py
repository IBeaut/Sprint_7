import requests
import random
import string

def generate_random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def register_new_courier_and_return_login_password():
    login = generate_random_string()
    password = generate_random_string()
    first_name = generate_random_string()

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        return [login, password, first_name]
    return []
