# -*- coding: UTF-8 -*-
# @Time: 2020-04-21 23:40
# @Author: wyd
# @File: ui_basic_oprate.py

from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# 全局等待 - 隐性等待
# driver.implicitly_wait(30)
# time.sleep(1)
# driver.maximize_window()
# time.sleep(1)
# driver.get('http://www.taobao.com')
# time.sleep(1)
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.refresh()
# print(driver.title)
# print(driver.current_url)
# print(driver.current_window_handle)
# time.sleep(5)
# driver.quit()
#######################################################################################
# 3种等待方式：sleep、implicitly_wait、WebDriverWait
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# driver.find_element_by_xpath('//*[@id="u1"]//a[@name="tj_login"]').click()
#
# id = 'TANGRAM__PSP_10__footerULoginBtn'
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, id)))
#
# driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()

########################################################################################
# 3种切换方式
# driver = webdriver.Chrome(service_log_path='/Users/wangyadong/Desktop/王亚东/UI_log')
# driver.get('https://ke.qq.com/')
# driver.find_element_by_xpath('//div[@id="js-mod-header-login"]//a[@id="js_login"]').click()
# # 这里没有定位到
# driver.implicitly_wait(30)
# driver.find_element_by_xpath('//div[contains(@class,"mod-tab")]//a[text()="QQ登录"]').click()
#
# time.sleep(1)
# # 切换iframe，进入到另一个html 方式一
# driver.switch_to.frame("login_frame_qq")
# driver.switch_to.frame(driver.find_element_by_xpath('//iframe=[@name="login_frame_qq"]'))
# driver.find_element_by_id('switcher_plogin')
#
# # 方式二
# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it('login_frame_qq'))
# time.sleep(1)
#
# # 从iframe当中回到默认的页面当中
# driver.switch_to.default_content()

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://www.baidu.com/')
# driver.find_element_by_id('kw').send_keys('柠檬班')
# driver.find_element_by_id('su').click()
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@tpl="tieba_general"]//a')))
# handles = driver.window_handles
# print('目前的窗口总数是：{}'.format(handles))
# driver.find_element_by_xpath('//div[@tpl="tieba_general"]//a').click()  # //a[contains(text(),"吧_百度贴吧")]

# 窗口切换1:
# step1:获取窗口的总数以及句柄，返回的是一个列表对象。新打开的窗口，位于最后一个
# handles = driver.window_handles
# print(handles)
# print(driver.current_window_handle)
# # 切换
# driver.switch_to.window(driver.window_handles[-1])
# # 新的窗口页面操作
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'j_head_focus_btn')))
# driver.find_element_by_id('j_head_focus_btn').click()

# 窗口切换2:
# 使用new_window_is_opened，len(driver.window_handles) > len(self.current_handles)
# WebDriverWait(driver, 10).until(EC.new_window_is_opened(handles))
# handles = driver.window_handles
# print('打开新窗口后总数是：{}'.format(handles))
# driver.switch_to.window(handles[-1])
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'j_head_focus_btn')))
# driver.find_element_by_id('j_head_focus_btn').click()

# alert切换   不是html页面元素
# driver.get('/Users/wangyadong/fullStackPython/web/hhh.html')
# WebDriverWait(driver, 10).until(EC.alert_is_present())
# alert = driver.switch_to.alert
# # 打印弹出框的内容
# print(alert.text)
# # 关闭弹出框
# alert.accept()
# # alert.dismiss()

###########################################################################
# 鼠标操作
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://www.baidu.com')
# # 先找到鼠标要操作的元素
# ele = driver.find_element_by_xpath('//*[@id="u1"]//a[@name="tj_settingicon"]')
# # 实例化ActionChains类
# ac = ActionChains(driver)
# # 将鼠标操作添加到action列表中
# ac.move_to_element(ele)
# # 调用perform来执行鼠标操作
# ac.perform()

# 让下拉列表显示出来
# ActionChains(driver).move_to_element(ele).perform()
# # 选择下拉列表中的高级搜索
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//a[text()="高级搜索"]')))
# driver.find_element_by_xpath('//a[text()="高级搜索"]').click()
#
# # select类
# # 找到select元素
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//select[@name="ft"]')))
# select_ele = driver.find_element_by_xpath('//select[@name="ft"]')
# # 实例化select类
# s = Select(select_ele)
# # 方式一,通过下表选择值
# s.select_by_index(4)
# time.sleep(1)
# # 方式一,通过value选择值
# s.select_by_value('ppt')
# time.sleep(1)
# # 方式一,通过文本选择值
# s.select_by_visible_text('RTF 文件 （.rtf)')

##################################################################################################
# 键盘操作
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# driver.find_element_by_xpath('//input[@id="kw"]').send_keys('hhh', Keys.ENTER)
# driver.find_element_by_xpath().get_attribute()
# driver.find_element_by_xpath().text

###################################################################################################
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('柠檬班')
driver.find_element_by_id('su').click()
# 滚动条处理
# 找到要滚动到可视区域的元素
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="content_left"]//a[contains(text()," - 知乎")]')))
ele = driver.find_element_by_xpath('//div[@id="content_left"]//a[contains(text()," - 知乎")]')
# 使用js进行滚动操作，滚动到最下方。移动到元素element对象的"底端"与当前窗口的"底部"对齐；，不加false是顶部
driver.execute_script("arguments[0].scrollIntoView(false);", ele)

# js语句定位日期控件，例如12306
js = 'var ele=document.getElementById("train_date");ele.readOnly=false;ele.value="2020-06-18";'
driver.execute_script(js)

#####################################################################################
# win+google浏览器上传文件
import win32gui
import win32con
def upload_file(filepath):
    dialog = win32gui.FindWindow('#32770', '打开') # 一级窗口
    # 二级窗口
    comboxex32 = win32gui.FindWindowEx(dialog, 0, 'ComBoxEx32', None)
    # 三级窗口
    combox = win32gui.FindWindowEx(comboxex32, 0, 'ComBox', None)
    # 文本的输入窗口 - 四级
    edit = win32gui.FindWindowEx(combox, 0, 'Edit', None)
    # 打开按钮 - 二级窗口
    button = win32gui.FindWindowEx(dialog, 0, 'Button', '打开(&0)')

    # 输入文件地址
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)  # 发送文件路径
    # 点击打开按钮  提交文件
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
