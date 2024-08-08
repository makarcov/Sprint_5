from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:

    def test_registration_success(self, driver_registration_form, login, password):
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

    def test_registration_wrong_password_failed(self, driver_registration_form, login, wrong_password):
        driver_registration_form.find_element(*Locators.REG_LOGIN_INPUT_FIELD).send_keys(login)
        driver_registration_form.find_element(*Locators.REG_EMAIL_INPUT_FIELD).send_keys(login)
        driver_registration_form.find_element(*Locators.REG_PASSWORD_INPUT_FIELD).send_keys(wrong_password)
        driver_registration_form.find_element(*Locators.REG_REGISTRATION_BUTTON).click()
        assert driver_registration_form.find_element(*Locators.REG_ERROR).is_displayed()
