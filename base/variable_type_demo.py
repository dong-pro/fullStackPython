# 单行注释
count = 100
money = 10.09
name = "Kevin"

'''
    多行注释这么写？

    四格缩进，严重依赖缩进

    单行不超过80长度

    不要在逗号, 分号, 冒号前面加空格, 但应该在它们后面加(除了在行尾)
'''
print(name + "收取单号" + str(count))

# 0b开头是二进制整数
no = 0b0010001
print(no)

# 加r 原生字符串
book = r'learning\npython\tok'
print(book)

# 转义 \n换行   \t
book = 'learning\npython\tok'
print(book)

isSuccess = True
print(isSuccess)

b = 9 == 7
print(b)

# 类型判断
print(type(b))
print(isinstance(b, bool))