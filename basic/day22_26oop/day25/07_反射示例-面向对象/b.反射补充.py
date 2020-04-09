"""
getattr # 根据字符串的形式，去对象中找成员。
hasattr # 根据字符串的形式，去判断对象中是否有成员。
setattr # 根据字符串的形式，动态的设置一个成员（内存）
delattr # 根据字符串的形式，动态的删除一个成员（内存）
"""

import xx
#

setattr(xx, 'f2', lambda x: x + 1)
v8 = getattr(xx, 'f2')
v9 = v8(1)
print(v9)
#
# # delattr
delattr(xx, 'x1')
v10 = getattr(xx, 'x1')
print(v10)
