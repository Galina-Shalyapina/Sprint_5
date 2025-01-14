from helpers import BASE_URL, generate_unique_email, wait_for_element_visibility, register_user, open_registration_page
from locators import TestLocators

class TestRegistration:
    def test_successful_registration(self, driver):
        open_registration_page(driver)
        name = "test"
        lastname = "testov"
        cohort = "19"
        unique_email = generate_unique_email(name, lastname, cohort)
        password = "password"
        register_user(driver, name, unique_email, password)
        login_button = wait_for_element_visibility(driver, TestLocators.button_login)
        assert login_button.is_displayed(), "Не удалось перейти на страницу входа после успешной регистрации"

    def test_registration_with_incorrect_password(self, driver):
        open_registration_page(driver)
        name = "test_incorrect"
        lastname = "testov_incorrect"
        cohort = "19"
        unique_email = generate_unique_email(name, lastname, cohort)
        password = "pass" # Пароль короче 6 символов
        register_user(driver, name, unique_email, password)
        # Проверяем, что появилось сообщение об ошибке некорректного пароля
        assert driver.find_element(*TestLocators.notification_incorrect_password).is_displayed(), "Сообщение об ошибке некорректного пароля не отображается"
