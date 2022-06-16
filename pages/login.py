from selenium.webdriver.common.by import By
from time import sleep

from common.yaml_handle import yaml_config

"""打开登录页面"""
host = yaml_config['host']


class LoginPage:
    url = host + '/login.html'

    # 用户名
    username_locator = (By.XPATH, '//input[@type="text"]')
    # 密码
    passwd_locator = (By.XPATH, '//input[@type="password"]')
    # 按钮
    btn_locator = (By.XPATH, '//button[@type="button"]')

    def __init__(self, driver):
        self.driver = driver

    def login(self, user_name, user_pwd):
        self.driver.find_element(*self.username_locator).send_keys(user_name)
        self.driver.find_element(*self.passwd_locator).send_keys(user_pwd)
        sleep(2)
        self.driver.find_element(*self.btn_locator).click()
        sleep(1)

    # 提取未输入用户和密码错误信息
    def get_error_msg(self):
        elem = self.driver.find_elements(By.CLASS_NAME, 'ant-form-explain')
        text = [el.text for el in elem]
        return text

    # 加载url
    def load(self):
        self.driver.get(self.url)
        return self
