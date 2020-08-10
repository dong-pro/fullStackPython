# -*- coding: UTF-8 -*-
# @Time: 2020-05-24 16:31
# @Author: wyd
# @File: wangpan_demo.py
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
# 运行代码之前：
# 1、appium_server启动成功，处于监听状态
# 2、模拟器/真机必须能够被电脑识别，即adb devices能够识别到要操作的设备
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((MobileBy.ID, 'com.baidu.netdisk:id/dialog_button_confirm')))
# id  同意协议
driver.find_element_by_id("com.baidu.netdisk:id/dialog_button_confirm").click()
# class
# driver.find_element_by_class_name("android.widget.Button")
# # content-desc
# driver.find_element_by_accessibility_id()
# uiautomator
# driver.find_element_by_android_uiautomator(
#     'new UiSelector().clickable(true).resourceId("com.baidu.netdisk:id/BaiduLoginBtn").text("百度帐号登录")').click()
# 百度账号登录
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.ID, 'com.baidu.netdisk:id/BaiduLoginBtn')))
driver.find_element_by_id("com.baidu.netdisk:id/BaiduLoginBtn").click()
# 输入用户名
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.CLASS_NAME, 'android.widget.EditText')))
driver.find_element_by_class_name("android.widget.EditText").send_keys("493775366@qq.com")
# 下一步
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.CLASS_NAME, 'android.widget.Button')))
driver.find_element_by_class_name("android.widget.Button").click()
# 密码
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.CLASS_NAME, 'android.view.View')))
driver.find_element_by_xpath('//android.widget.EditText[@password="true"]').send_keys('wangyadong')
# 登录
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("登 录")')))
driver.find_element_by_android_uiautomator('new UiSelector().text("登 录")').click()
# 设置完成
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((MobileBy.ID, 'com.baidu.netdisk:id/setDone')))
driver.find_element_by_id('com.baidu.netdisk:id/setDone').click()
