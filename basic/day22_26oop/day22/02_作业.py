# -*- coding:UTF-8 -*-
# @Time: 2019/9/6 15:00
# @Author: wyd
# @File: 02_作业.py

import math

class Demo:

    def __init__(self, r):
        self.r = r

    def zhouchang(self):
        zhouchang = self.r * 2 * math.pi
        print('圆的周长是%s' % zhouchang)

    def mianji(self):
        mianji = self.r ** 2 * math.pi
        print('圆的周长是%s' % mianji)

obj = Demo(3)
obj.zhouchang()
obj.mianji()