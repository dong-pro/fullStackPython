# -*- coding: UTF-8 -*-
# @Time: 2020-05-12 21:47
# @Author: wyd
# @File: dir_config.py

import os

base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# 测试数据路径
testdata_dir = os.path.join(base_dir, 'TestDatas')

# 测试用例路径
testcase_dir = os.path.join(base_dir, 'TestCases')

# html报告路径
htmlreport_dir = os.path.join(base_dir, 'Outputs/reports')

# log路径
log_dir = os.path.join(base_dir, 'Outputs/logs')

# 截图路径
screenshot_dir = os.path.join(base_dir, 'Outputs/screenshots')