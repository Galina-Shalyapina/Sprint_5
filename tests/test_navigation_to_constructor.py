from helpers import wait_for_element_visibility, open_main_page
from locators import TestLocators

class TestNavigationToConstructor:
    def test_go_to_buns_section(self, driver):
        """Проверяет переход к разделу 'Булки'."""
        open_main_page(driver)
        # Сначала переходим в раздел "Соусы", чтобы раздел "Булки" стал кликабельным
        sauces_block = wait_for_element_visibility(driver, TestLocators.sauces_block)
        sauces_block.click()
        # Убеждаемся, что раздел "Булки" виден и кликабелен
        buns_block = wait_for_element_visibility(driver, TestLocators.buns_block)
        buns_block.click()
        # Проверяем, что селектор активного раздела отображается рядом с разделом "Булки"
        assert driver.find_element(*TestLocators.selected_button).text == "Булки"

    def test_go_to_sauces_section(self, driver):
        """Проверяет переход к разделу 'Соусы'."""
        open_main_page(driver)
        # Убеждаемся, что раздел "Соусы" виден и кликабелен
        sauces_block = wait_for_element_visibility(driver, TestLocators.sauces_block)
        sauces_block.click()
        # Проверяем, что селектор активного раздела отображается рядом с разделом "Соусы"
        assert driver.find_element(*TestLocators.selected_button).text == "Соусы"

    def test_go_to_fillings_section(self, driver):
        """Проверяет переход к разделу 'Начинки'."""
        open_main_page(driver)
        # Убеждаемся, что раздел "Начинки" виден и кликабелен
        fillings_block = wait_for_element_visibility(driver, TestLocators.fillings_block)
        fillings_block.click()
        # Проверяем, что селектор активного раздела отображается рядом с разделом "Начинки"
        assert driver.find_element(*TestLocators.selected_button).text == "Начинки"

    def test_go_to_sauces_from_fillings_section(self, driver):
        """Проверяет переход к разделу 'Соусы' после выбора 'Начинки'."""
        open_main_page(driver)
        # Переходим в раздел "Начинки"
        driver.find_element(*TestLocators.fillings_block).click()
        assert driver.find_element(*TestLocators.selected_button).text == "Начинки"
        # Переходим в раздел "Соусы"
        driver.find_element(*TestLocators.sauces_block).click()
        assert driver.find_element(*TestLocators.selected_button).text == "Соусы"

    def test_go_to_fillings_from_sauces_section(self, driver):
        """Проверяет переход к разделу 'Начинки' после выбора 'Соусы'."""
        open_main_page(driver)
        # Переходим в раздел "Соусы"
        driver.find_element(*TestLocators.sauces_block).click()
        assert driver.find_element(*TestLocators.selected_button).text == "Соусы"
        # Переходим в раздел "Начинки"
        driver.find_element(*TestLocators.fillings_block).click()
        assert driver.find_element(*TestLocators.selected_button).text == "Начинки"

    def test_go_to_buns_from_fillings_section(self, driver):
        """Проверяет переход к разделу 'Булки' после выбора 'Начинки'."""
        open_main_page(driver)
        # Переходим в раздел "Начинки"
        driver.find_element(*TestLocators.fillings_block).click()
        assert driver.find_element(*TestLocators.selected_button).text == "Начинки"
        # Переходим в раздел "Булки"
        driver.find_element(*TestLocators.buns_block).click()
        assert driver.find_element(*TestLocators.selected_button).text == "Булки"
