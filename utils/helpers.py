import requests
import random
import string

def generate_random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_user_data():
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }

def register_courier(data):
    return requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=data)
