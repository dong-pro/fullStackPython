# 2
# def func(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     return sum
# print(func(1, 5, 7))

# def func(*args):  # args是元组. 可以迭代
#     return sum(args)
#
# print(sum([3, 5, 7]))  # sum中可以直接接受一个可迭代对象. 他会把这个可迭代对象进行迭代. 把每个元素累加
# print(func(1, 5, 7))

# a = 10
# b = 20
# def test5(a, b):
#     print(a, b)  # None
# c = test5(b, a)
# print(c)  # None

# a = 10
# b = 20
# def test5(a, b):
#     a = 3
#     b = 5
# print(a, b)  # 10 20
# c = test5(20, 10)
# print(c)  # None
# print(a, b)  # 10, 20

# def func(*args):
#     print(args)
# func(1, 4, 7, 9, '你', '好', '啊')
# func(*[1, 4, 7, 9], *'你好啊')

# def wrapper():
#     a = 1
#     print(a)
#     def inner():
#         nonlocal a
#         a += 1
#         print(a)
#     inner()
#     print(a)
# wrapper()

# def fun(a, b):
#     return a if a < b else b

# def func(lst=[1, 'admin', 'root']):
#     s = ''
#     for el in lst:
#         s = s + str(el) + '_'
#     return s.rstrip('_')
#
# print(func())


# def func(*args):
#     return {'max': max(args), 'min': min(args)}
#
# print(func(1, 7, 9, 3, 6, -5, 4))
#
# def func(n):
#     sum = 1
#     while n >= 1:
#         sum = sum * n
#         n = n - 1
#     return sum
# print(func(5))

# def func():
#     result = []
#     huase = ['红心', '黑桃', '草花', '方片']
#     dianshu = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
#
#     for hua in huase:
#         for dian in dianshu:
#             result.append((hua, dian))
#     return result
# print(func())

# def calc(a, b, c, d=1, e=2):  # 12314
#     return (a+b)*(c-d)+e

# 请分别写出下列标号代码的输出结果，如果出错请写出Error。
# print(calc(1,2,3,4,5))#_____
# print(calc(1,2))#____
# print(calc(e=4,c=5,a=2,b=3))#___
# print(calc(1,2,3))#_____
# print(calc(1,2,3,e=4))#____
# print(calc(1,2,3,d=5,4))#_____

# def extendList(val, list=[]):  # 默认值如果是可变的数据类型. 每次使用的时候都是同一个
#     print(id(list))
#     list.append(val)
#     return list
#
#
# list1 = extendList(10)
# list2 = extendList(123, [])
# list3 = extendList('a')
#
# print('list1=%s' % list1)
# print('list2=%s' % list2)
# print('list3=%s' % list3)

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('*', end=' ')
#     print()  # 打印空

# *
# **
# ***
# ****
# *****
# ******
#
#      *
#     ***
#    *****
#     ***
#      *
#
# def regist():
#     print('欢迎进入注册系统')
#     while 1:
#         username = input('请输入用户名:').strip()
#         password = input('请输入密码:').strip()
#         if username == '' or password == '':
#             print('用户名或者密码不合法')
#             continue
#
#         # 校验用户名是否已经存在
#         f = open('db.log', mode='r+', encoding='utf-8')
#         for line in f:  # sylar@@123456
#             if username == line.split('@@')[0]:
#                 print('对不起, 该用户名已经被注册. 请重新注册')
#                 break
#         else:  # 没注册过
#             f.write('\n'+username+'@@'+password)
#             print('注册成功了')
#             return
#
# regist()