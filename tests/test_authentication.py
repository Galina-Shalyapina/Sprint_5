import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from locators import TestLocators
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestAuthentication(unittest.TestCase):
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

    def test_login_from_main_page(self):
        name = "auth_test1"
        lastname = "auth_testov1"
        cohort = "30"
        email = self.generate_unique_email(name, lastname, cohort)
        password = "password"
        self.register_user(name, email, password)
        self.driver.get(self.BASE_URL)
        self.driver.find_element(*TestLocators.button_login_in_main).click()
        self.login_user(email, password)
        try:
            wait = WebDriverWait(self.driver, 10)
            make_order_button = wait.until(EC.visibility_of_element_located(TestLocators.button_make_the_order))
            self.assertTrue(make_order_button.is_displayed(), "Не удалось войти через кнопку 'Войти в аккаунт' на главной")
        except TimeoutException:
            self.fail("Кнопка 'Оформить заказ' не появилась на странице после входа через главную в течение 10 секунд")

    def test_login_from_personal_account(self):
        name = "auth_test2"
        lastname = "auth_testov2"
        cohort = "31"
        email = self.generate_unique_email(name, lastname, cohort)
        password = "password"
        self.register_user(name, email, password)
        self.driver.get(self.BASE_URL)
        self.driver.find_element(*TestLocators.button_personal_account).click()
        self.login_user(email, password)
        try:
            wait = WebDriverWait(self.driver, 10)
            make_order_button = wait.until(EC.visibility_of_element_located(TestLocators.button_make_the_order))
            self.assertTrue(make_order_button.is_displayed(), "Не удалось войти через кнопку 'Личный кабинет'")
        except TimeoutException:
            self.fail("Кнопка 'Оформить заказ' не появилась на странице после входа через личный кабинет в течение 10 секунд")

    def test_login_from_registration_form(self):
        name = "auth_test3"
        lastname = "auth_testov3"
        cohort = "32"
        email = self.generate_unique_email(name, lastname, cohort)
        password = "password"
        self.register_user(name, email, password)
        self.driver.get(self.BASE_URL)
        self.driver.find_element(*TestLocators.button_personal_account).click()
        self.driver.find_element(*TestLocators.button_register).click()
        self.driver.find_element(*TestLocators.button_login_in_registration_form).click()
        self.login_user(email, password)
        try:
            wait = WebDriverWait(self.driver, 10)
            make_order_button = wait.until(EC.visibility_of_element_located(TestLocators.button_make_the_order))
            self.assertTrue(make_order_button.is_displayed(), "Не удалось войти через кнопку в форме регистрации")
        except TimeoutException:
            self.fail("Кнопка 'Оформить заказ' не появилась на странице после входа через форму регистрации в течение 10 секунд")

    def test_login_from_forgot_password_form(self):
        name = "auth_test4"
        lastname = "auth_testov4"
        cohort = "33"
        email = self.generate_unique_email(name, lastname, cohort)
        password = "password"
        self.register_user(name, email, password)
        self.driver.get(self.BASE_URL)
        self.driver.find_element(*TestLocators.button_personal_account).click()
        self.driver.find_element(*TestLocators.button_forgot_password).click()
        self.driver.find_element(*TestLocators.button_login_passwd_recovery_form).click()
        self.login_user(email, password)
        try:
            wait = WebDriverWait(self.driver, 10)
            make_order_button = wait.until(EC.visibility_of_element_located(TestLocators.button_make_the_order))
            self.assertTrue(make_order_button.is_displayed(), "Не удалось войти через кнопку в форме восстановления пароля")
        except TimeoutException:
            self.fail("Кнопка 'Оформить заказ' не появилась на странице после входа через форму восстановления пароля в течение 10 секунд")