#issubclass
# class Base(object):
#     pass
#
# class Foo(Base):
#     pass
#
# class Bar(Foo):
#     pass
#
# print(issubclass(Bar, Base))  # 检查第一个参数是否是第二个参数的 子子孙孙类


# #type
# class Foo(object):
#     pass
#
# obj = Foo()
# print(obj, type(obj))  # 获取当前对象是由那个类创建。
# if type(obj) == Foo:
#     print('obj是Foo类型')
# #### 练习题
# class Foo(object):
#     pass
# class Bar(object):
#     pass
# def func(*args):
#     foo_counter = 0
#     bar_counter = 0
#     for item in args:
#         if type(item) == Foo:
#             foo_counter += 1
#         elif type(item) == Bar:
#             bar_counter += 1
#     return foo_counter, bar_counter
#
# result = func(Foo(), Bar(), Foo())
# print(result)
# v1, v2 = func(Foo(), Bar(), Foo())
# print(v1, v2)


# #isinstance
class Base(object):
    pass
class Foo(Base):
    pass
obj1 = Foo()
print(isinstance(obj1, Foo))  # 检查第一个参数（对象）是否是第二个参数（类及父类）的实例。
print(isinstance(obj1, Base))  # 检查第一个参数（对象）是否是第二个参数（类及父类）的实例。
obj2 = Base()
print(isinstance(obj2, Foo))  # 检查第一个参数（对象）是否是第二个参数（类及父类）的实例。
print(isinstance(obj2, Base))  # 检查第一个参数（对象）是否是第二个参数（类及父类）的实例。

# #################### 练习
"""
给你一个参数，判断对象是不是由某一个指定类？ type                  --> type(obj) == Foo
给你一个参数，判断对象是不是由某一个指定类或其父类？ isinstance    --> instance(obj,Foo)
"""
