# -*- coding: UTF-8 -*-
# @Time: 2020-05-05 17:44
# @Author: wyd
# @File: bidpage_locators.py

from selenium.webdriver.common.by import By

class BidPageLocator(object):
    # 元素定位
    # 可用余额输入框
    money_input = (By.XPATH, '//input[contains(@class,"invest-unit-investinput")]')
    # 投标按钮
    invest_but = (By.XPATH, '//button[text()="投标"]')
    #  查看并激活按钮
    active_button_on_success_popup = (By.XPATH, '//button[text()="查看并激活"]')
    # 投资失败的提示
    invest_failed_popup = (By.XPATH, '')
    # 投资失败的提示
    invest_close_failed_popup_button = (By.XPATH, '')
