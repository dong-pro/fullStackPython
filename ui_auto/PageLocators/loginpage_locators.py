# -*- coding: UTF-8 -*-
# @Time: 2020-05-03 23:54
# @Author: wyd
# @File: loginpage_locators.py

from selenium.webdriver.common.by import By

class LoginPageLocator(object):
    # 元素定位
    # 用户名输入框
    name_text = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    pwd_text = (By.XPATH, '//input[@name="password"]')
    # 登录按钮
    login_but = (By.XPATH, '//button[text()="登录"]')
    # 错误提示框
    errorMsg_from_loginArea = (By.XPATH, '//div[@class="form-error-info"]')
    errorMsg_from_conterArea = (By.XPATH, '//div[@class="layui-layer-content"]')
