from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructorSection:

    def test_construction_buns_success(self, driver):
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.BUNS_BUTTON))
        element = driver.find_element(*Locators.BUNS_BUTTON)
        driver.execute_script("arguments[0].click();", element)
        status = driver.find_element(*Locators.BUNS_BUTTON).get_attribute('class')
        check_word = 'current'
        assert check_word in status

    def test_construction_sauces_success(self, driver):
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.SAUCES_BUTTON))
        element = driver.find_element(*Locators.SAUCES_BUTTON)
        driver.execute_script("arguments[0].click();", element)
        status = driver.find_element(*Locators.SAUCES_BUTTON).get_attribute('class')
        check_word = 'current'
        assert check_word in status

    def test_construction_fillings_success(self, driver):
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.FILLINGS_BUTTON))
        element = driver.find_element(*Locators.FILLINGS_BUTTON)
        driver.execute_script("arguments[0].click();", element)
        status = driver.find_element(*Locators.FILLINGS_BUTTON).get_attribute('class')
        check_word = 'current'
        assert check_word in status

