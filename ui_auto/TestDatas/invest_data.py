# -*- coding: UTF-8 -*-
# @Time: 2020-05-12 22:43
# @Author: wyd
# @File: invest_data.py

# 正常场景 - 测试数据
success_data = {
    'money': 600,
}

# 异常场景 - 手机号格式不正确(<>11位，为空，不在号码段)
wrong_data = {
    'money': 130,
    'check': '',
}
