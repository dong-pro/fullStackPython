# -*- coding: UTF-8 -*-
# @Time: 2020-05-05 16:36
# @Author: wyd
# @File: bid_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui_auto.PageLocators.bidpage_locators import BidPageLocator as loc
from ui_auto.Common.basepage import BasePage


class BidPage(BasePage):

    # 投资
    def invest(self, money):
        # 在输入框中输入金额
        doc = '标详情页面_投资操作'
        self.wait_eleVisible(loc.money_input, doc)
        self.input_text(loc.money_input, money, doc)
        # 点击投标按钮
        self.click_element(loc.invest_but, doc)

    # 获取用户余额
    def get_user_money(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.money_input))
        return self.driver.find_element(*loc.money_input).get_attribute("data-amount")

    # 投资成功的提示框：点击查看并激活
    def click_activeButton_on_success_popup(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.active_button_on_success_popup))
        self.driver.find_element(*loc.active_button_on_success_popup).click()

    # 错误的提示框：页面中间
    def get_errorMsg_from_pageCenter(self):
        # 获取文本内容
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.invest_failed_popup))
        msg = self.driver.find_element(*loc.invest_failed_popup).text
        # 关闭弹出框
        self.driver.find_element(*loc.invest_close_failed_popup_button).click()
        return msg

    # 获取提示信息：投标按钮上的
    def get_errorMsg_from_investButton(self):
        pass
