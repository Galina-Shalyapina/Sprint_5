from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import TestLocators


class TestConstructorSections:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        self.driver.quit()

    def test_go_to_buns_section(self):
        """Проверяет переход к разделу 'Булки'."""
        # Сначала переходим в раздел "Соусы", чтобы раздел "Булки" стал кликабельным
        sauces_block = self.wait.until(EC.visibility_of_element_located(TestLocators.sauces_block))
        sauces_block.click()
        # Убеждаемся, что раздел "Булки" виден и кликабелен
        buns_block = self.wait.until(EC.visibility_of_element_located(TestLocators.buns_block))
        buns_block.click()
        # Проверяем, что селектор активного раздела отображается рядом с разделом "Булки"
        assert self.driver.find_element(*TestLocators.selected_button).text == "Булки"

    def test_go_to_sauces_section(self):
        """Проверяет переход к разделу 'Соусы'."""
        # Убеждаемся, что раздел "Соусы" виден и кликабелен
        sauces_block = self.wait.until(EC.visibility_of_element_located(TestLocators.sauces_block))
        sauces_block.click()
        # Проверяем, что селектор активного раздела отображается рядом с разделом "Соусы"
        assert self.driver.find_element(*TestLocators.selected_button).text == "Соусы"

    def test_go_to_fillings_section(self):
        """Проверяет переход к разделу 'Начинки'."""
        # Убеждаемся, что раздел "Начинки" виден и кликабелен
        fillings_block = self.wait.until(EC.visibility_of_element_located(TestLocators.fillings_block))
        fillings_block.click()
        # Проверяем, что селектор активного раздела отображается рядом с разделом "Начинки"
        assert self.driver.find_element(*TestLocators.selected_button).text == "Начинки"

    def test_go_to_sauces_from_fillings_section(self):
        """Проверяет переход к разделу 'Соусы' после выбора 'Начинки'."""
        # Переходим в раздел "Булки"
        self.driver.find_element(*TestLocators.fillings_block).click()
        assert self.driver.find_element(*TestLocators.selected_button).text == "Начинки"
        # Переходим в раздел "Соусы"
        self.driver.find_element(*TestLocators.sauces_block).click()
        assert self.driver.find_element(*TestLocators.selected_button).text == "Соусы"

    def test_go_to_fillings_from_sauces_section(self):
        """Проверяет переход к разделу 'Начинки' после выбора 'Соусы'."""
        # Переходим в раздел "Соусы"
        self.driver.find_element(*TestLocators.sauces_block).click()
        assert self.driver.find_element(*TestLocators.selected_button).text == "Соусы"
        # Переходим в раздел "Начинки"
        self.driver.find_element(*TestLocators.fillings_block).click()
        assert self.driver.find_element(*TestLocators.selected_button).text == "Начинки"

    def test_go_to_buns_from_fillings_section(self):
        """Проверяет переход к разделу 'Булки' после выбора 'Начинки'."""
        # Переходим в раздел "Начинки"
        self.driver.find_element(*TestLocators.fillings_block).click()
        assert self.driver.find_element(*TestLocators.selected_button).text == "Начинки"
        # Переходим в раздел "Булки"
        self.driver.find_element(*TestLocators.buns_block).click()
        assert self.driver.find_element(*TestLocators.selected_button).text == "Булки"