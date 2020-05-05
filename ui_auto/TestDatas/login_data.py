# -*- coding: UTF-8 -*-
# @Time: 2020-05-03 16:19
# @Author: wyd
# @File: login_data.py

# 正常场景 - 测试数据
success_data = {
    'user': '13825161923',
    'password': 'lemon123'
}

# 异常场景 - 手机号格式不正确(<>11位，为空，不在号码段)
phone_data = [
    {
        'user': '138251619',
        'password': 'lemon123',
        'check': '请输入正确的手机号'
    },
    {
        'user': '1382516192345',
        'password': 'lemon123',
        'check': '请输入正确的手机号'
    },
    {
        'user': '',
        'password': 'lemon123',
        'check': '请输入手机号'
    },
    {
        'user': '11125161923',
        'password': 'lemon123',
        'check': '请输入正确的手机号'
    },
    {
        'user': '13825161923',
        'password': '',
        'check': '请输入密码'
    },
]

# 异常场景 - 密码错误，手机号未注册
password_data = [
    {
        'user': '13825161923',
        'password': '123',
        'check': '帐号或密码错误!'
    },
    {
        'user': '13899998888',
        'password': 'lemon123',
        'check': '此账号没有经过授权，请联系管理员!'
    },
]
