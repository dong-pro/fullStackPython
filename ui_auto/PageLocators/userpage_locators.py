# -*- coding: UTF-8 -*-
# @Time: 2020-05-05 18:24
# @Author: wyd
# @File: userpage_locators.py

from selenium.webdriver.common.by import By


class UserPageLocator(object):
    # 元素定位
    # 用户余额
    user_leftMoney = (By.XPATH, '//input[@name="phone"]')
