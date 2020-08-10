# -*- coding: UTF-8 -*-
# @Time: 2020-06-11 17:09
# @Author: wyd
# @File: toast获取.py

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time

desired_caps = {}
# 自动化测试引擎
desired_caps["automationName"] = "UiAutomator2"
# 平台类型
desired_caps["platformName"] = "Android"
# 平台版本号
desired_caps["platformVersion"] = "7.1.2"
# 设备名称
desired_caps["deviceName"] = "Android Emulator"
# app包名
desired_caps["appPackage"] = "com.baidu.netdisk"
# app入口activity
desired_caps["appActivity"] = "com.baidu.netdisk.ui.Navigate"

# 连接appium_server。前提：appium_desktop要启动，有监听端口。
# 将desired_caps发送给appium_server，打开app
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 同意协议
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((MobileBy.ID, 'com.baidu.netdisk:id/dialog_button_confirm')))
driver.find_element_by_id("com.baidu.netdisk:id/dialog_button_confirm").click()

# 微信快捷登录
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.ID, 'com.baidu.netdisk:id/wxLoginBtn')))
driver.find_element_by_id('com.baidu.netdisk:id/wxLoginBtn').click()
# xpath表达式 文本匹配
loc = (MobileBy.XPATH, '//*[contains(@text,"微信未安装")]')
# 等待的时候，要用元素存在的条件presence_of_element_located，不能用元素可见的条件
try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(loc))
    print(driver.find_element_by_xpath('//*[contains(@text,"微信未安装")]').text)
except:
    print('没有找到匹配的toast')
