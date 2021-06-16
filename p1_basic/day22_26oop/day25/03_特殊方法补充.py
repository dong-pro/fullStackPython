# #str
# class Foo(object):
#     def __init__(self):
#         pass
#
#     def func(self):
#         pass
#
#     def __str__(self):
#         return "F1"
#
# obj = Foo()
# print(obj, type(obj))


# #doc
# class Foo(object):
#     """
#     asdfasdfasdfasdf
#     """
#     def __init__(self):
#         pass
#
#     def func(self):
#         pass
#
#     def __str__(self):
#         return "F1"
#
# obj = Foo()
# print(obj.__doc__)

# # dict
# class Foo(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def func(self):
#         pass
#
# obj1 = Foo('刘博文', 99)
# obj2 = Foo('史雷', 89)
#
# print(obj1.__dict__)  # {'name': '刘博文', 'age': 99}
# print(obj2.__dict__)  # {'name': '史雷', 'age': 89}

# #iter
# class Foo(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def func(self):
#         pass
#
# # obj1是Foo类的一个对象，不可迭代对象
# obj1 = Foo('刘博文', 99)
#
# for item in obj1:
#     print(item)

# l1是list类的一个对象，可迭代对象
l1 = [11, 22, 33, 44]
# l2是list类的一个对象，可迭代对象
l2 = [1, 22, 3, 44]

class Foo(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func(self):
        pass

    def __iter__(self):
        # return iter([11,22,33,44,55,66])

        yield 11
        yield 22
        yield 33
# obj1是Foo类的一个对象，可迭代对象

"""
如果想要把不可迭代对象 -> 可迭代对象
1. 在类中定义__iter__方法
2. iter内部返回一个迭代器(生成器也是一种特殊迭代器)
"""
obj1 = Foo('刘博文', 99)

for item in obj1:
    print(item)
