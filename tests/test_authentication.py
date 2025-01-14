from helpers import open_main_page, wait_for_element_visibility, login_user, open_profile_page, \
    open_registration_page, open_forgot_password_page
from locators import TestLocators

class TestAuthentication:
    def test_login_from_main_page(self, driver, registered_user):
        email, password = registered_user
        open_main_page(driver)
        driver.find_element(*TestLocators.button_login_in_main).click()
        login_user(driver, email, password)
        make_order_button = wait_for_element_visibility(driver, TestLocators.button_make_the_order)
        assert make_order_button.is_displayed(), "Не удалось войти через кнопку 'Войти в аккаунт' на главной"

    def test_login_from_personal_account(self, driver, registered_user):
        email, password = registered_user
        open_profile_page(driver)
        login_user(driver, email, password)
        make_order_button = wait_for_element_visibility(driver, TestLocators.button_make_the_order)
        assert make_order_button.is_displayed(), "Не удалось войти через кнопку 'Личный кабинет'"

    def test_login_from_registration_form(self, driver, registered_user):
        email, password = registered_user
        open_registration_page(driver)
        driver.find_element(*TestLocators.button_login_in_registration_form).click()
        login_user(driver, email, password)
        make_order_button = wait_for_element_visibility(driver, TestLocators.button_make_the_order)
        assert make_order_button.is_displayed(), "Не удалось войти через кнопку в форме регистрации"

    def test_login_from_forgot_password_form(self, driver, registered_user):
        email, password = registered_user
        open_forgot_password_page(driver)
        driver.find_element(*TestLocators.button_login_passwd_recovery_form).click()
        login_user(driver, email, password)
        make_order_button = wait_for_element_visibility(driver, TestLocators.button_make_the_order)
        assert make_order_button.is_displayed(), "Не удалось войти через кнопку в форме восстановления пароля"
