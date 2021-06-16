# 第一题：

# class StarkConfig(object):
#     list_display = []
#
#     def get_list_display(self):
#         self.list_display.insert(0, 33)
#         return self.list_display
#
# class RoleConfig(StarkConfig):
#     list_display = [11, 22]
#
# s1 = StarkConfig()

# result1 = s1.get_list_display()
# print(result1)  # 33
#
# result2 = s1.get_list_display()
# print(result2)  # 33 33

# class StarkConfig(object):
#     def __init__(self):
#         self.list_display = []
#
#     def get_list_display(self):
#         self.list_display.insert(0, 33)
#         return self.list_display
#
#
# class RoleConfig(StarkConfig):
#     list_display = [11, 22]
#
#
# s1 = StarkConfig()
#
# result1 = s1.get_list_display()
# print(result1)  # 33
#
# result2 = s1.get_list_display()
# print(result2)  # 33 33


# class StarkConfig(object):
#     def __init__(self):
#         self.list_display = []
#
#     def get_list_display(self):
#         self.list_display.insert(0, 33)
#         return self.list_display
#
# class RoleConfig(StarkConfig):
#     list_display = [11, 22]
#
# s1 = StarkConfig()
# s2 = StarkConfig()
#
# result1 = s1.get_list_display()
# print(result1)  # 33
#
# result2 = s2.get_list_display()
# print(result2)  # 33

# class StarkConfig(object):
#     list_display = []
#
#     def get_list_display(self):
#         self.list_display.insert(0, 33)
#         return self.list_display
#
# class RoleConfig(StarkConfig):
#     list_display = [11, 22]
#
# s1 = StarkConfig()
# s2 = StarkConfig()
#
# result1 = s1.get_list_display()
# print(result1)  # 33
#
# result2 = s2.get_list_display()
# print(result2)  # 33 33
# ############################################################################################

# 第四题：
class StarkConfig(object):
    list_display = []

    def get_list_display(self):
        self.list_display.insert(0, 33)
        return self.list_display

class RoleConfig(StarkConfig):
    list_display = [11, 22]

s1 = RoleConfig()
s2 = RoleConfig()
result1 = s1.get_list_display()
print(result1)
result2 = s2.get_list_display()
print(result2)