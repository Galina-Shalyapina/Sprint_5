import unittest

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from data import UsersTestData
from locators import TestLocators

class TestLogout(unittest.TestCase):
    BASE_URL = "https://stellarburgers.nomoreparties.site/"

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get(self.BASE_URL)
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def login(self):
        """Метод для логина пользователя."""
        self.driver.find_element(*TestLocators.button_login_in_main).click()
        self.driver.find_element(*TestLocators.input_email_auth).send_keys(UsersTestData.email)
        self.driver.find_element(*TestLocators.input_password_auth).send_keys(UsersTestData.password)
        self.driver.find_element(*TestLocators.button_login).click()

    def test_logout_from_profile_button(self):
        """Проверка выхода из аккаунта по кнопке «Выйти» в личном кабинете."""
        self.login()  # Сначала логинимся

        # Переходим в личный кабинет
        self.driver.find_element(*TestLocators.button_personal_account).click()

        try:
            # Нажимаем кнопку "Выйти"
            self.wait.until(EC.visibility_of_element_located(TestLocators.button_logout))
            self.driver.find_element(*TestLocators.button_logout).click()

            # Проверяем, что произошел выход из аккаунта, ожидая исчезновения кнопки "Личный Кабинет"
            button_login = self.wait.until(EC.visibility_of_element_located(TestLocators.button_login))

            # Теперь проверяем, что отображается кнопка "Войти"
            self.assertTrue(button_login.is_displayed())
        except TimeoutException:
            self.fail("Не удалось выйти из аккаунта")
