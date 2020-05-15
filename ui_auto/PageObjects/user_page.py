# -*- coding: UTF-8 -*-
# @Time: 2020-05-05 18:23
# @Author: wyd
# @File: user_page.py

from ui_auto.Common.basepage import BasePage
from ui_auto.PageLocators.userpage_locators import UserPageLocator as loc


class UserPage(BasePage):

    # 获取用户余额
    def get_user_leftMoney(self):
        doc = '个人页面_获取用户余额'
        # 等待元素
        self.wait_eleVisible(loc.user_leftMoney, doc=doc)
        # 获取个人可用余额的文本内容
        text = self.get_text(loc.user_leftMoney, doc=doc)
        # 截取数据部分 - 分隔符为 元
        return text.strip('元')
