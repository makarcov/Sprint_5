from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestEnterAccount:

    def test_login_via_enter_account_button_success(self, driver, login, password):
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.ENTER_REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.REG_LOGIN_INPUT_FIELD).send_keys(login)
        driver.find_element(*Locators.REG_EMAIL_INPUT_FIELD).send_keys(login)
        driver.find_element(*Locators.REG_PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.REG_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
        driver.find_element(*Locators.LOGO_BUTTON).click()
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.ENTER_EMAIL_INPUT_FIELD).send_keys(login)
        driver.find_element(*Locators.ENTER_PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.MAKE_ORDER_BUTTON))
        assert driver.find_element(*Locators.MAKE_ORDER_BUTTON).is_displayed()

    def test_login_via_personal_account_button_success(self, driver, login, password):
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.ENTER_REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.REG_LOGIN_INPUT_FIELD).send_keys(login)
        driver.find_element(*Locators.REG_EMAIL_INPUT_FIELD).send_keys(login)
        driver.find_element(*Locators.REG_PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.REG_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
        driver.find_element(*Locators.LOGO_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.ENTER_EMAIL_INPUT_FIELD).send_keys(login)
        driver.find_element(*Locators.ENTER_PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.MAKE_ORDER_BUTTON))
        assert driver.find_element(*Locators.MAKE_ORDER_BUTTON).is_displayed()

    def test_login_via_registration_enter_button_success(self, driver_registration_form, login, password):
        driver_registration_form.find_element(*Locators.REG_LOGIN_INPUT_FIELD).send_keys(login)
        driver_registration_form.find_element(*Locators.REG_EMAIL_INPUT_FIELD).send_keys(login)
        driver_registration_form.find_element(*Locators.REG_PASSWORD_INPUT_FIELD).send_keys(password)
        driver_registration_form.find_element(*Locators.REG_REGISTRATION_BUTTON).click()
        WebDriverWait(driver_registration_form, 5).until(
            expected_conditions.visibility_of_element_located(Locators.ENTER_BUTTON))
        driver_registration_form.find_element(*Locators.ENTER_EMAIL_INPUT_FIELD).send_keys(login)
        driver_registration_form.find_element(*Locators.ENTER_PASSWORD_INPUT_FIELD).send_keys(password)
        driver_registration_form.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver_registration_form, 5).until(
            expected_conditions.visibility_of_element_located(Locators.MAKE_ORDER_BUTTON))
        assert driver_registration_form.find_element(*Locators.MAKE_ORDER_BUTTON).is_displayed()

    def test_login_via_enter_forgot_password_button_success(self, driver, login, password):
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.ENTER_REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.REG_LOGIN_INPUT_FIELD).send_keys(login)
        driver.find_element(*Locators.REG_EMAIL_INPUT_FIELD).send_keys(login)
        driver.find_element(*Locators.REG_PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.REG_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
        driver.find_element(*Locators.LOGO_BUTTON).click()
        driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.ENTER_FORGOT_PASSWORD_BUTTON).click()
        driver.find_element(*Locators.FORGOT_PASSWORD_ENTER_BUTTON).click()
        driver.find_element(*Locators.ENTER_EMAIL_INPUT_FIELD).send_keys(login)
        driver.find_element(*Locators.ENTER_PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.MAKE_ORDER_BUTTON))
        assert driver.find_element(*Locators.MAKE_ORDER_BUTTON).is_displayed()
