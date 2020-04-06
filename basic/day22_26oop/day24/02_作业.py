# -*- coding:UTF-8 -*-
# @Time: 2019/9/9 16:18
# @Author: wyd
# @File: 02_作业.py

# 1.简述⾯向对象三⼤特性并⽤示例解释说明
# 封装
# class Foo(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         pass
#
#     def read(self):
#         print('读%s' % self.name)
#
#     def write(self):
#         print('写%s' % self.age)
#
# obj = Foo('kkk', 18)
# obj.read()
# obj.write()
#
# # 继承
# class Zi(Foo):
#     def __init__(self, name, age, phone):
#         self.name = name
#         self.age = age
#         self.phone = phone
#         pass
#
#     def add(self):
#         print('改%s' % self.phone)
#
# obj = Zi('ppp', 77, 1111111)
# obj.write()

# 2.⾯向中的变量分为哪⼏种？并⽤示例说明区别？
# 实例变量: 公有、私有
# class Foo(object):
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age
#     def func(self):
#         print(self.__name)
#         print(self.age)
# obj = Foo('kkk', 88)
# obj.func()
# print(obj.age)
# 类变量: 公有、私有
# class Foo(object):
#     address = '北京'
#     __add2 = '上海'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def func(self):
#         print(Foo.address)
#         print(Foo.__add2)
#
# obj = Foo('kkk', 88)
# obj.func()
# print(Foo.address)

# 3.⾯向对象中⽅法有哪⼏种？并⽤示例说明区别？
# 实例方法: 公有、私有
# class Foo(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __func(self):
#         print(self.name)
#     def func2(self):
#         print(333)
#         self.__func()
# obj = Foo('kkk', 99)
# # obj.func()
# obj.func2()

# 静态方法: 公有、私有
# class Foo(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def func(a, b):
#         print(a + b)
#         Foo.__func2(5, 6)
#
#     @staticmethod
#     def __func2(c, d):
#         print(c * d)
# obj = Foo('kkk', 44)
# obj.func(3, 4)

# 类方法: 公有、私有
# class Foo(object):
#
#     def __init__(self):
#         pass
#     @classmethod
#     def func(cls, a, b):
#         print(a+b)
#         cls.__func2(5, 4)
#
#     @classmethod
#     def __func2(cls, a, b):
#         print(a + b)
# obj = Foo()
# obj.func(1, 2)
# Foo.func(3, 4)

# 4.⾯向对象中的属性有什么？并⽤示例说明？
# class Foo(object):
#     @property
#     def start(self):
#         return 11
#     def end(self):
#         return 'yyy'
# obj = Foo()
# print(obj.start)

# 9. 999  11   11   print(Foo.a2)报错

# 10
# 666   1  baocuo  baocuo 1  baocuo
# 11
#666 1  18  99  1  1000  1098
# 12
# class Foo(object):
#     hobby = '大保健'
#     def __init__(self, num):
#         self.num = num
#         self.__salary = 1000
#
#     def f1(self):
#         print(Foo.hobby)
#         print(self.num)
#
#     @staticmethod
#     def f2():
#         print(Foo.hobby)
#
#     @classmethod
#     def f3(cls):
#         print(obj.f1())
#
# obj = Foo(33)
# obj.f2()
# Foo.f3()

# 13
# class Base(object):
#     @classmethod
#     def f3(cls):
#         print(cls)
#     def f1(self):
#         print('Base.f1')
#         self.f3()
#
# class Foo(Base):
#
#     def f2(self):
#         print('Foo.f2')
#         self.f1()
#
# obj = Foo()
# obj.f2()



class School:
    def __init__(self, address):
        self.address = address

bj = School('北京校区')
sh = School('上海校区')
sz = School('深圳校区')

class Course(object):
    def __init__(self, name, period, price, school=None):
        self.name = name
        self.period = period
        self.price = price
        self.school = school

py1 = Course('Python全栈', 110, 19999, bj)
py2 = Course('Python全栈', 110, 19999, sh)
py3 = Course('Python全栈', 110, 19999, sz)

l1 = Course('Linux运维', 110, 19999, bj)
l2 = Course('Linux运维', 110, 19999, sh)

g1 = Course('Go开发', 119, 19999, bj)

class Grade(object):
    def __init__(self, name, people, introduce, course=None):
        self.name = name
        self.people = people
        self.introduce = introduce
        self.course = course

gr1 = Grade('全栈1期', 20, '....', py1)
gr2 = Grade('全栈1期', 20, '....', py2)

gr3 = Grade('Linux8期', 20, '....', l2)

gr1.people
gr1.course.price
gr1.course.school.address

