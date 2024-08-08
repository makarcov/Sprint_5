from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestGoToConstructor:

    def test_go_constructor_via_button_success(self, driver, login, password):
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
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_BUTTON))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))
        assert driver.find_element(*Locators.CONSTRUCTOR_TITLE).is_displayed()

    def test_go_constructor_via_logo_success(self, driver, login, password):
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
            expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
        driver.find_element(*Locators.LOGO_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))
        assert driver.find_element(*Locators.CONSTRUCTOR_TITLE).is_displayed()