# -*- coding: UTF-8 -*-
# @Time: 2020-05-03 14:04
# @Author: wyd
# @File: login_page.py

from ui_auto.PageLocators.loginpage_locators import LoginPageLocator as loc
from ui_auto.Common.basepage import BasePage

class LoginPage(BasePage):

    # 登录
    def login(self, username, password, remeber_user=True):
        doc = '登录页面_登录功能'
        self.wait_eleVisible(loc.name_text, doc=doc)
        self.input_text(loc.name_text, username, doc=doc)
        self.input_text(loc.pwd_text, password, doc=doc)
        # 判断一下remember_user的值，来决定是否勾选.这里还没写
        if remeber_user:
            pass
        # 判断处理是在用例里面写的，这里面只是写登录操作。容易混淆
        self.click_element(loc.login_but, doc=doc)

    # 注册.这里还没写
    def register(self):
        pass

    # 忘记密码.这里还没写
    def forget_pwd(self):
        pass

    # 获取错误提示信息 - 登录区域
    def get_errorMsg_from_loginArea(self):
        doc = '登录页面_获取登录区域的错误提示'
        self.wait_eleVisible(loc.errorMsg_from_loginArea, doc=doc)
        return self.get_text(loc.errorMsg_from_loginArea, doc=doc)

    # 获取错误提示信息 - 中心区域
    def get_errorMsg_from_conterArea(self):
        doc = '登录页面_获取登录区域的错误提示'
        self.wait_eleVisible(loc.errorMsg_from_conterArea, doc=doc)
        return self.get_text(loc.errorMsg_from_conterArea, doc=doc)
