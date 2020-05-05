# -*- coding: UTF-8 -*-
# @Time: 2020-05-03 14:04
# @Author: wyd
# @File: index_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui_auto.PageLocators.indexpage_locators import IndexPageLocator as loc
import random

class IndexPage(object):

    def __init__(self, driver):
        self.driver = driver

    def isExist_logut_ele(self):
        # 如果存在就返回True，不存在就返回False
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(loc.logout_but))
            return True
        except:
            return False

    # 选标操作：默认选第一个。元素定位的时候，过滤掉不可以投的标
    def click_first_bid(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.bid_but))
        self.driver.find_element(*loc.bid_but).click()

    def click_bid_by_random(self):
        # 找到所有符合的标
        eles = self.driver.find_elements()
        # 随机数
        index = random.randint(0, len(eles)-1)
        eles[index].click()
