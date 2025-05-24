import pytest

@pytest.fixture(scope="session")
def base_url():
    return "https://qa-scooter.praktikum-services.ru"
