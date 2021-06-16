# ### 1. 类或对象是否能做字典的key
# class Foo:
#     pass
#
# user_info = {
#     Foo: 1,
#     Foo(): 5
# }
# print(user_info)

# ### 2. 对象中到底有什么?
# class Foo(object):
#     def __init__(self, age):
#         self.age = age
#
#     def display(self):
#         print(self.age)
#
# data_list = [Foo(8), Foo(9)]
#
# for item in data_list:
#     print(item.age, item.display())

# ### 3.
# class StarkConfig(object):
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
# class RoleConfig(StarkConfig):
#     def changelist(self, request):
#         print('666')
#
# # 创建了一个列表,列表中有三个对象(实例)
# [ StarkConfig对象(num=1), StarkConfig对象(num=2), RoleConfig对象(num=3) ]
# config_obj_list = [StarkConfig(1), StarkConfig(2), RoleConfig(3)]
# for item in config_obj_list:
#     print(item.num)  # 1 2 3

# ### 4.
# class StarkConfig(object):
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
# class RoleConfig(StarkConfig):
#     pass
#
# # 创建了一个列表,列表中有三个对象(实例)
# # [ StarkConfig对象(num=1), StarkConfig对象(num=2), RoleConfig对象(num=3) ]
# config_obj_list = [StarkConfig(1), StarkConfig(2), RoleConfig(3)]
# for item in config_obj_list:
#     item.changelist(168)

# #### 5
# class StarkConfig(object):
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
# class RoleConfig(StarkConfig):
#
#     def changelist(self, request):
#         print(666, self.num)
#
# # 创建了一个列表,列表中有三个对象(实例)
# # [ StarkConfig对象(num=1), StarkConfig对象(num=2), RoleConfig对象(num=3) ]
# config_obj_list = [StarkConfig(1), StarkConfig(2), RoleConfig(3)]
# for item in config_obj_list:
#     item.changelist(168)

# #### 6
# class StarkConfig(object):
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#     def run(self):
#         self.changelist(999)
#
# class RoleConfig(StarkConfig):
#     def changelist(self, request):
#         print(666, self.num)
#
# config_obj_list = [StarkConfig(1), StarkConfig(2), RoleConfig(3)]
# config_obj_list[1].run()
# config_obj_list[2].run()  # 666 3
# #### 8

### 9
# class StarkConfig(object):
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#     def run(self):
#         self.changelist(999)
#
# class RoleConfig(StarkConfig):
#     def changelist(self, request):
#         print(666, self.num)
#
# class AdminSite(object):
#     def __init__(self):
#         self._registry = {}
#
#     def register(self, k, v):
#         self._registry[k] = v
#
# site = AdminSite()
# site.register('lyd', StarkConfig(19))
# site.register('yjl', StarkConfig(20))
# site.register('fgz', RoleConfig(33))
# print(len(site._registry))  # 3
# print(site._registry)  # 3
#
# for k, row in site._registry.items():
#     row.run()

## 10
class UserInfo(object):
    pass
class Department(object):
    pass
class StarkConfig(object):
    def __init__(self, num):
        self.num = num
    def changelist(self, request):
        print(self.num, request)
    def run(self):
        self.changelist(999)
class RoleConfig(StarkConfig):
    def changelist(self, request):
        print(666, self.num)
class AdminSite(object):
    def __init__(self):
        self._registry = {}
    def register(self, k, v):
        self._registry[k] = v(k)
site = AdminSite()
site.register(UserInfo, StarkConfig)
site.register(Department, StarkConfig)
# print(len(site._registry))  # 3
print(site._registry)
for k, row in site._registry.items():
    row.run()

# 总结:
"""
1. 对象中封装了什么?
2. self到底是谁?
"""
