# -*- coding: UTF-8 -*-
# @Time: 2020-05-12 21:43
# @Author: wyd
# @File: run.py

import unittest
from ui_auto.Common import dir_config
from ui_auto.Common.HTMLTestRunner import HTMLTestRunner

# 实例化套件对象
suite = unittest.TestSuite()
# TestLoader的用法
# 1、实例化TestLoader对象
# 2、使用discover去找到一个目录下的所有测试用例
# 3、使用suite
loader = unittest.TestLoader()
suite.addTests(loader.discover(dir_config.testcase_dir))
# 运行
# runner = unittest.TextTestRunner()
# runner.run(suite)

fp = open(dir_config.htmlreport_dir + '/autoTest_report.html', 'wb')
runner = HTMLTestRunner(stream=fp, title='webUI自动化', description='测试专用')
runner.run(suite)
