import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from locators import TestLocators
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestRegistration(unittest.TestCase):
    EMAIL_DOMAIN = "@yandex.ru"
    BASE_URL = "https://stellarburgers.nomoreparties.site/"

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get(self.BASE_URL)

    def tearDown(self):
        self.driver.quit()

    def generate_unique_email(self, name, lastname, cohort):
        random_digits = ''.join(random.choices('0123456789', k=3))
        return f"{name}_{lastname}_{cohort}_{random_digits}{self.EMAIL_DOMAIN}"

    def register_user(self, name, email, password):
        self.driver.find_element(*TestLocators.button_personal_account).click()
        self.driver.find_element(*TestLocators.button_register).click()
        self.driver.find_element(*TestLocators.input_name).send_keys(name)
        self.driver.find_element(*TestLocators.input_email).send_keys(email)
        self.driver.find_element(*TestLocators.input_password).send_keys(password)
        self.driver.find_element(*TestLocators.button_submit).click()

    def login_user(self, email, password):
        self.driver.find_element(*TestLocators.input_email_auth).send_keys(email)
        self.driver.find_element(*TestLocators.input_password_auth).send_keys(password)
        self.driver.find_element(*TestLocators.button_login).click()

    def test_successful_registration(self):
        name = "test"
        lastname = "testov"
        cohort = "19"
        unique_email = self.generate_unique_email(name, lastname, cohort)
        password = "password"
        self.register_user(name, unique_email, password)

        try:
            wait = WebDriverWait(self.driver, 10)
            login_button = wait.until(EC.visibility_of_element_located(TestLocators.button_login))
            self.assertTrue(login_button.is_displayed(), "Не удалось перейти на страницу входа после успешной регистрации")
        except TimeoutException:
            self.fail("Кнопка 'Войти' не появилась на странице после регистрации в течение 10 секунд")

    def test_registration_with_incorrect_password(self):
        name = "test"
        lastname = "testov"
        cohort = "19"
        unique_email = self.generate_unique_email(name, lastname, cohort)
        password = "pass" # Пароль короче 6 символов
        self.register_user(name, unique_email, password)
        # Проверяем, что появилось сообщение об ошибке некорректного пароля
        self.assertTrue(self.driver.find_element(*TestLocators.notification_incorrect_password).is_displayed(), "Сообщение об ошибке некорректного пароля не отображается")