# -*- coding: UTF-8 -*-
# @Time: 2019-09-15 15:48
# @Author: wyd
# @File: 06_日志.py

import logging

# logger = logging.basicConfig(filename='xxxxxxx.txt',
#                              format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#                              datefmt='%Y-%m-%d %H:%M:%S',
#                              level=30)
#
# logging.debug('x1')  # 10
# logging.info('x2')  # 20
# logging.warning('x3')  # 30
# logging.error('x4')  # 40
# logging.critical('x5')  # 50
# logging.log(10,'x6')
#
import traceback
#
# def func():
#     try:
#         a = a + 1
#     except Exception as e:
#         # 获取当前错误的堆栈信息
#         msg = traceback.format_exc()
#         logging.error(msg)
# #
# func()


# class Foo:
#     def __str__(self):
#         return 'asdfadfasdfasd'
# obj = Foo()
# print(obj, type(obj))
#
# v1 = str(obj)
# print(v1)


# 日志文件个数。再写一个logger2不会生效，也是忘logger1中写日志。这里需要自定义日志
# logger1 = logging.basicConfig(filename='x1.txt',
#                               format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#                               datefmt='%Y-%m-%d %H:%M:%S',
#                               level=30)
#
# logging.error('x4')
# logging.error('x5')

# #自定义日志
# 创建一个操作日志的对象logger（依赖FileHandler）
file_handler = logging.FileHandler('l1.log', 'a', encoding='utf-8')
file_handler.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s"))

logger1 = logging.Logger('s1', level=logging.ERROR)
logger1.addHandler(file_handler)

logger1.error('123123123')

# 在创建一个操作日志的对象logger（依赖FileHandler）
file_handler2 = logging.FileHandler('l2.log', 'a', encoding='utf-8')
file_handler2.setFormatter(logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s"))

logger2 = logging.Logger('s2', level=logging.ERROR)
logger2.addHandler(file_handler2)

logger2.error('666')