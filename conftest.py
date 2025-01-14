import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from helpers import generate_unique_email, BASE_URL, register_user


@pytest.fixture()
def driver():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

@pytest.fixture()
def registered_user(driver):
    name = "auth_test"
    lastname = "auth_testov"
    cohort = "13"
    email = generate_unique_email(name, lastname, cohort)
    password = "password"
    driver.get(BASE_URL)
    register_user(driver, name, email, password)
    yield email, password
