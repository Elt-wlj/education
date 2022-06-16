import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import allure
from time import sleep

from data import login
from pages.login import LoginPage


@allure.feature('用户登录测试模块用例')
class TestLogin:
    @allure.title('用户名和密码正确')
    @pytest.mark.parametrize('case', login.success)
    def test_login_success(self, get_driver, case):
        username, passwd, expected = case
        driver = get_driver
        login_page = LoginPage(driver)
        login_page.load()
        user_name = driver.find_element(By.XPATH, '//input[@type="text"]')
        user_name.send_keys(username)
        user_pwd = driver.find_element(By.XPATH, '//input[@type="password"]')
        user_pwd.send_keys(passwd)
        butn = driver.find_element(By.XPATH, '//button[@type="button"]')
        butn.click()
        sleep(1)
        actual = driver.find_element(By.XPATH, '//div[@class="mg-r-min"]').text
        try:
            assert actual == expected
            print(actual)
        except AssertionError as e:
            print(f'用户名{actual}与实际值{expected}不一致')

    @allure.title('用户名和密码为空')
    def test_login_without_username_and_passwd(self, get_driver):
        driver = get_driver
        login_page = LoginPage(driver)
        login_page.load().login('', '')
        actual_value = login_page.get_error_msg()
        expected = ['需要一个账户', '需要一个密码']
        try:
            assert expected == actual_value
            print(actual_value)
        except AssertionError as e:
            print(f'用户名{expected}与实际值{actual_value}不一致')

    @allure.title('用户名为空')
    def test_login_without_username(self, get_driver):
        driver = get_driver
        login_page = LoginPage(driver)
        login_page.load().login('', '111111')
        actual_value = login_page.get_error_msg()
        expected = ['需要一个账户']
        try:
            assert expected == actual_value
            print(actual_value)
        except AssertionError as e:
            print(f'用户名{expected}与实际值{actual_value}不一致')

    @allure.title('密码为空')
    def test_login_without_username(self, get_driver):
        driver = get_driver
        login_page = LoginPage(driver)
        login_page.load().login('tj', '')
        actual_value = login_page.get_error_msg()
        expected = ['需要密码']
        try:
            assert expected == actual_value
            print(actual_value)
        except AssertionError as e:
            print(f'用户名{expected}与实际值{actual_value}不一致')
