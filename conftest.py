# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture()
def driver():
    # Путь к исполняемому файлу ChromeDriver (укажите свой путь)
    chromedriver_path = 'path/to/chrome/driver'
    service = ChromeService(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()