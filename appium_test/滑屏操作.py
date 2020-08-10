# -*- coding: UTF-8 -*-
# @Time: 2020-06-09 22:50
# @Author: wyd
# @File: 滑屏操作.py

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
desired_caps["appPackage"] = "com.tencent.mobileqq"
# app入口activity
desired_caps["appActivity"] = "com.tencent.mobileqq.activity.SplashActivity"
# 重置与否
desired_caps["noReset"] = True

# 连接appium_server。前提：appium_desktop要启动，有监听端口。
# 将desired_caps发送给appium_server，打开app
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
loc = (MobileBy.ID, 'com.tencent.mobileqq:id/j_k')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(loc))
size = driver.get_window_size()
start_x = size['width'] * 0.9
start_y = size['height'] * 0.5

end_x = size['width'] * 0.1
end_y = size['height'] * 0.5
# 从右向左滑
# driver.swipe(start_x, start_y, end_x, end_y, 200)
# 从左向右滑
time.sleep(1)
driver.swipe(end_x, end_y, start_x, start_y, 200)

# 上下滑动
# 向上滑动：X轴不变，Y轴从大到小
# driver.swipe(size['width'] * 0.5, size['height'] * 0.9, size['width'] * 0.5, size['height'] * 0.1, 200)
