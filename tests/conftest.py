import pytest
import random
from selenium import webdriver

@pytest.fixture # Фикстура для запуска
def driver():
    return webdriver.Chrome()

@pytest.fixture # Фикстура для driver.find_element
def find(driver):
    find = driver.find_element
    return find

@pytest.fixture # Фикстура со ссылкой на тестовый стенд
def website():
    return "https://qa-desk.stand.praktikum-services.ru/"

@pytest.fixture # Фикстура для генерации случайного email
def random_email():
    first_names = ["alex", "michael", "john", "sarah", "anna", "david", "olga", "maria", "andrey", "oleg", "max", "pavel", "benedict"]
    last_names = ["smith", "johnson", "williams", "brown", "jones", "miller", "davis", "ermakova", "sazonova", "cumberbatch"]
    number = random.randint(1, 9999)
    domains = ["gmail.com", "yahoo.com", "mail.ru", "yandex.ru", "example.com"]
    return f'{random.choice(first_names)}_{random.choice(last_names)}{number}@{random.choice(domains)}'

@pytest.fixture # Фикстура для пароля
def password():
    password = "ABfqa-2sFU"
    return password

@pytest.fixture # Фикстура для использования email уже зарегистрированного юзера
def test_mail():
    test_mail = "test2222@test.ru"
    return test_mail
