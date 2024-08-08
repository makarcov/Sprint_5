import pytest
import selenium
from selenium import webdriver
from data import Data
from helpers import Helpers
from locators import Locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# драйвер, запускающий главную страницу
@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1920,1080)
    driver.get(Data.MAIN_PAGE_BURGERS)
    yield driver
    driver.quit()

# драйвер, запускающий страницу регистрации
@pytest.fixture(scope='function')
def driver_registration_form(driver):
    driver.find_element(*Locators.ENTER_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.ENTER_REGISTRATION_BUTTON).click()
    yield driver
    driver.quit()

@pytest.fixture()
def login():
    return Helpers.generate_login()

@pytest.fixture()
def password():
    return Helpers.generate_password()

@pytest.fixture()
def wrong_password():
    return Helpers.generate_wrong_password()
