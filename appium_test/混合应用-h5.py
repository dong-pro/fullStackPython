# -*- coding: UTF-8 -*-
# @Time: 2020-06-11 18:49
# @Author: wyd
# @File: 混合应用-h5.py

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time

desired_caps = {}
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
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((MobileBy.ID, 'com.baidu.netdisk:id/dialog_button_confirm')))
# id  同意协议
driver.find_element_by_id("com.baidu.netdisk:id/dialog_button_confirm").click()
# 百度账号登录
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.ID, 'com.baidu.netdisk:id/BaiduLoginBtn')))
driver.find_element_by_id("com.baidu.netdisk:id/BaiduLoginBtn").click()

# 等待webview元素出现 -html
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy,'')))
time.sleep(1)

# 前提：代码可以识别到webview，需要开启app的webview debug属性
# context 就是原生控件
# 1.先列出所有的context
cons = driver.contexts
print(cons)
# 2.切换到webview.要确保chromedriver的版本与webview匹配，也要放置在对应的位置
driver.switch_to.context(cons[-1])

# 3.切换之后：当前的操作对象--html页面
# 等待元素可见
