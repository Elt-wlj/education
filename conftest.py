from selenium import webdriver
import pytest


@pytest.fixture()
def get_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()