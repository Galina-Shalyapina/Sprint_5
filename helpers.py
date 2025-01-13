import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import TestLocators

EMAIL_DOMAIN = "@yandex.ru"
BASE_URL = "https://stellarburgers.nomoreparties.site/"

def generate_unique_email(name, lastname, cohort):
    random_digits = ''.join(random.choices('0123456789', k=6))
    return f"{name}_{lastname}_{cohort}_{random_digits}{EMAIL_DOMAIN}"

def open_main_page(driver):
    driver.get(BASE_URL)

def wait_for_element_visibility(driver, locator, timeout=10):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.visibility_of_element_located(locator))

def register_user(driver, name, email, password):
    driver.find_element(*TestLocators.button_personal_account).click()
    driver.find_element(*TestLocators.button_register).click()
    driver.find_element(*TestLocators.input_name).send_keys(name)
    driver.find_element(*TestLocators.input_email).send_keys(email)
    driver.find_element(*TestLocators.input_password).send_keys(password)
    driver.find_element(*TestLocators.button_submit).click()

def open_registration_page(driver):
    driver.get(BASE_URL)
    driver.find_element(*TestLocators.button_personal_account).click()
    driver.find_element(*TestLocators.button_register).click()

def login_user(driver, email, password):
    driver.find_element(*TestLocators.input_email_auth).send_keys(email)
    driver.find_element(*TestLocators.input_password_auth).send_keys(password)
    driver.find_element(*TestLocators.button_login).click()

def open_login_page(driver):
    driver.get(BASE_URL)
    driver.find_element(*TestLocators.button_login_in_main).click()

def open_profile_page(driver):
    driver.get(BASE_URL)
    driver.find_element(*TestLocators.button_personal_account).click()

def open_forgot_password_page(driver):
    open_profile_page(driver)
    driver.find_element(*TestLocators.button_forgot_password).click()