# -*- coding: UTF-8 -*-
# @Time: 2020-05-05 18:33
# @Author: wyd
# @File: basepage.py
'''
1、封装基本函数：执行日志，异常处理，失败截图
2、所有的页面公共的部分（和系统业务无关）
'''

import logging
import datetime
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui_auto.Common import dir_config


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, locator, timeout=30, poll_frequency=0.5, doc=''):
        '''
        :param locator: 页面元素定位。元组形式（元素定位类型，元素定位方式）
        :param timeout: 页面查找元素时最多的等待时间
        :param poll_frequency: 每隔多久查询一次页面元素
        :param doc: 模块名_页面名称_操作名称
        :return: None
        '''
        logging.info('{0}等待元素{1}可见'.format(doc, locator))
        try:
            # 开始等待的时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待的时间
            end = datetime.datetime.now()
            # 求一个差值，写在日志当中，等待了多久
            wait_time = (end - start).seconds
            logging.info('等待结束，等待时长为{}秒'.format(wait_time))
        except:
            logging.exception('等待元素可见失败！！！')
            # 截图
            self.save_screenshot(doc)
            raise

    # 等待元素存在
    def wait_elePreseence(self):
        # 还没写
        pass

    # 查找元素
    def get_element(self, locator, doc=''):
        '''
        :param locator: 页面元素定位。元组形式（元素定位类型，元素定位方式）
        :param doc: 模块名_页面名称_操作名称
        :return:
        '''
        logging.info('{0}查找元素{1}'.format(doc, locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception('查找元素失败！！！')
            # 截图
            self.save_screenshot(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc=''):
        # 找元素
        ele = self.get_element(locator, doc)
        # 元素操作
        logging.info('{0}点击元素{1}'.format(doc, locator))
        try:
            ele.click()
        except:
            logging.exception('元素点击操作失败！！！')
            # 截图
            self.save_screenshot(doc)
            raise

    # 输入操作
    def input_text(self, locator, text, doc=''):
        # 找元素
        ele = self.get_element(locator, doc)
        # 输入操作
        logging.info('{0}输入元素{1}'.format(doc, locator))
        try:
            ele.send_keys(text)
        except:
            logging.exception('元素输入操作失败！！！')
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素的文本内容
    def get_text(self, locator, doc=''):
        # 找元素
        ele = self.get_element(locator, doc)
        # 获取元素的文本内容
        logging.info('{0}获取元素的文本内容{1}'.format(doc, locator))
        try:
            return ele.text
        except:
            logging.exception('获取元素文本内容失败！！！')
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素的属性
    def get_element_attribute(self, locator, attr, doc=''):
        # 找元素
        ele = self.get_element(locator, doc)
        # 获取元素的属性
        logging.info('{0}获取元素的属性{1}'.format(doc, locator))
        try:
            return ele.get_attribute(attr)
        except:
            logging.exception('获取元素属性失败！！！')
            # 截图
            self.save_screenshot(doc)
            raise

    # alert处理
    def alert_action(self, action='accept'):
        pass

    # iframe切换
    def switch_iframe(self, iframe_reference):
        pass

    # 上传操作
    def upload_file(self):
        pass

    # 滚动条处理
    # 窗口切换

    def save_screenshot(self, doc):
        # 图片名称：模块名_页面名称_操作名称_年-月-日_时分秒.png
        src_name = '{0}_{1}.png'.format(doc, datetime.datetime.now().strftime('%Y-%m-%d_%H%S%M'))
        file_path = os.path.join(dir_config.screenshot_dir, src_name)
        try:
            self.driver.save_screenshot(file_path)
            logging.info('截取网页成功，文件路径是：{}'.format(file_path))
        except:
            logging.exception('截图失败')

