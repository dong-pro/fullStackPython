# -*- coding: UTF-8 -*-
# @Time: 2020-05-04 10:13
# @Author: wyd
# @File: indexpage_locators.py

from selenium.webdriver.common.by import By

class IndexPageLocator(object):
    # 元素定位
    # 退出按钮
    logout_but = (By.XPATH, '//a[text()="退出"]')
    # 抢投标按钮
    bid_but = (By.XPATH, '//a[text()="抢投标"]')
