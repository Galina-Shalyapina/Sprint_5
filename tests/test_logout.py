from helpers import wait_for_element_visibility, login_user, open_main_page
from locators import TestLocators


def test_logout_from_profile_button(driver, registered_user):
    """Проверка выхода из аккаунта по кнопке «Выйти» в личном кабинете."""
    email, password = registered_user
    open_main_page(driver)
    driver.find_element(*TestLocators.button_login_in_main).click()
    login_user(driver, email, password)  # Сначала логинимся
    # Переходим в личный кабинет
    driver.find_element(*TestLocators.button_personal_account).click()
    # Нажимаем кнопку "Выйти"
    wait_for_element_visibility(driver, TestLocators.button_logout)
    driver.find_element(*TestLocators.button_logout).click()

    # Проверяем, что произошел выход из аккаунта, ожидая появления кнопки "Войти"
    button_login = wait_for_element_visibility(driver, TestLocators.button_login)

    # Теперь проверяем, что отображается кнопка "Войти"
    assert button_login.is_displayed()
