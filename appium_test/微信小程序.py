# -*- coding: UTF-8 -*-
# @Time: 2020-06-11 21:38
# @Author: wyd
# @File: 微信小程序.py

'''
启动appium时，需要指定chromedriver.exe的目录。使用appium默认目录下的会报错。
在切换到小程序webview时，回去匹配chrome内核的39的驱动。在切换完成之后，在打印所有的窗口
所以指定一个非默认目录下面的chromedriver.exe（X5内核对应的版本），此问题就不会出现。
在appium server上设置chromedriver的路径
'''

