# -*- coding: UTF-8 -*-
# @Time: 2020-06-09 23:21
# @Author: wyd
# @File: 触屏操作.py

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
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
# 重置与否
desired_caps["noReset"] = True

# 连接appium_server。前提：appium_desktop要启动，有监听端口。
# 将desired_caps发送给appium_server，打开app
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
ele = driver.find_element_by_id('')
# 元素的大小
size = ele.size
# 均分的步长，高和宽一样
step = size['width'] / 6
# 元素的起点坐标 - 左上角
ori = ele.location
point_1 = (ori['x'] + step, ori['y'] + step)
point_2 = (point_1[0] + step * 2, point_1[1])  # 相对于point1，x轴增加了2*step
point_3 = (point_2[0] + step * 2, point_2[1])  # 相对于point2，x轴增加了2*step
point_4 = (point_3[0] - step * 2, point_3[1] + step * 2)  # 相对于point3，x轴减少了2*step，y轴增加了2*step
point_5 = (point_4[0], point_4[1] + step * 2)  # 相对于point4，y轴增加了2*step

TouchAction(driver).press(x=point_1[0], y=point_1[1]).wait(200).move_to(x=point_2[0], y=point_2[1]).wait(200).move_to(
    x=point_3[0], y=point_3[1]).wait(200).move_to(x=point_4[0], y=point_4[1]).wait(200).move_to(x=point_5[0],
                                                                                                y=point_5[1]).wait(
    200).release().perform()
