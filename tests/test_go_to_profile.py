import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from locators import TestLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestGoToProfile(unittest.TestCase):
    BASE_URL = "https://stellarburgers.nomoreparties.site/"

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get(self.BASE_URL)

    def tearDown(self):
        self.driver.quit()

    def test_go_to_personal_account_unauthorized(self):
        """Проверяет переход в личный кабинет для неавторизованного пользователя."""
        self.driver.find_element(*TestLocators.button_personal_account).click()
        try:
            wait = WebDriverWait(self.driver, 10)
            login_button = wait.until(EC.visibility_of_element_located(TestLocators.button_login))
            self.assertTrue(login_button.is_displayed(), "Не произошло перехода на страницу входа после клика на 'Личный кабинет'")
        except TimeoutException:
            self.fail("Не дождались появления кнопки 'Войти' на странице входа")