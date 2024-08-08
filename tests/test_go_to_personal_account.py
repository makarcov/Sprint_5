from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestEnterPersonalAccount:

    def test_enter_personal_account_success(self, driver, login, password):
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
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.SAVE_BUTTON))
        profile_name = driver.find_element(*Locators.PROFILE_TITLE).get_attribute('value')
        assert profile_name == login
