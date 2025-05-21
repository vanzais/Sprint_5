import pytest
import random
import string
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('https://qa-desk.stand.praktikum-services.ru/')
    yield driver
    driver.quit()


@pytest.fixture
def random_email():
    random_name = ''.join(random.choices(string.ascii_lowercase, k=12))
    random_domain = ''.join(random.choices(string.ascii_lowercase, k=6))
    random_tld = random.choice(['com', 'ru', 'org', 'net'])
    email = f'{random_name}@{random_domain}.{random_tld}'
    return email

@pytest.fixture
def random_email_error():
    return ''.join(random.choices(string.ascii_lowercase, k=15))

