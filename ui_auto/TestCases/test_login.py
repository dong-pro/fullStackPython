# -*- coding: UTF-8 -*-
# @Time: 2020-05-03 14:28
# @Author: wyd
# @File: test_login.py

import unittest
import ddt
from selenium import webdriver
from ui_auto.PageObjects.login_page import LoginPage
from ui_auto.PageObjects.index_page import IndexPage
from ui_auto.TestDatas import common_data
from ui_auto.TestDatas import login_data

'''
1.数据分离:多环境切换；数据公用；好维护 - TestDatas
2.测试用例 - ddt的引用，降低重复率
3.优化了执行效率 - setUpClass、tearDownClass。每条用例之间互不影响
4.元素定位分离：元素定位类型和表达式用元组来管理 - PageLocators层
'''
@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 前置条件 访问登录页面
        print('====={}测试用例开始执行====='.format(__file__))
        cls.driver = webdriver.Chrome()
        cls.driver.get(common_data.web_login_url)
        cls.lg = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        # 后置
        print('====={}测试用例结束执行====='.format(__file__))
        cls.driver.quit()

    # def setUp(self):
    #     pass

    def tearDown(self):
        # 每个用例执行完后刷新页面
        self.driver.refresh()

    # 正常用例 - 登录成功
    def test_login_2_success(self):
        # 步骤 输入用户名密码点击登录
        self.lg.login(login_data.success_data['user'], login_data.success_data['password'])
        # 断言 首页当中能否找到  退出 这个元素
        self.assertTrue(IndexPage(self.driver).isExist_logut_ele())

    # 异常用例 - 手机号格式不正确(<>11位，为空，不在号码段)
    @ddt.data(*login_data.phone_data)
    def test_login_0_user_wrongFormat(self, data):
        # 步骤 输入用户名密码点击登录
        self.lg.login(data['user'], data['password'])
        # 断言 登录首页 输入框下面提示：
        # 登录页面中 - 获取提示框的文本内容。然后比对文本内容与期望的值是否相等
        self.assertEqual(self.lg.get_errorMsg_from_loginArea(), data['check'])

    @ddt.data(*login_data.password_data)
    def test_login_1_password_wrongFormat(self, data):
        # 步骤 输入用户名密码点击登录
        # 断言 登录首页 页面正中间提示：
        # 登录页面中 - 获取提示框的文本内容。然后比对文本内容与期望的值是否相等
        self.lg.login(data['user'], data['password'])
        self.assertEqual(self.lg.get_errorMsg_from_conterArea(), data['check'])
