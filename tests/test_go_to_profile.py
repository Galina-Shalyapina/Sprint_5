from helpers import open_main_page, wait_for_element_visibility
from locators import TestLocators

class TestGoToProfile:
    def test_go_to_personal_account_unauthorized(self, driver):
        """Проверяет переход в личный кабинет для неавторизованного пользователя."""
        open_main_page(driver)
        driver.find_element(*TestLocators.button_personal_account).click()
        login_button = wait_for_element_visibility(driver, TestLocators.button_login)
        assert login_button.is_displayed(), "Не произошло перехода на страницу входа после клика на 'Личный кабинет'"
