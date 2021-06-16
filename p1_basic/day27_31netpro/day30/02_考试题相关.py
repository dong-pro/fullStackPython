# ########## 第10题
v = [lambda: x for x in range(10)]
print(v)
print(v[0])
print(v[0]())

# 1.Python中函数时一个作用域；打印？报错

# 正确
# i = 0
# for i in range(10):
#     pass
# 44444444444444444444444
# print(i)  # 9

# 报错
# def func():
#     for i in range(10):
#         pass
#
# func()
# print(i)

# 2.lambda表达式
# def f1(x):
#     return x + i
#
# func_list = []
# i = 0
# for i in range(10):
#     func_list.append(f1)
# 4444444444444444444444444444444444444
# # 此时i=9  执行函数：内部调用函数代码
# print(func_list[5](8))

# 3.列表生成式
# val = [lambda x:x+i for i in range(10)]
# ret = val[3](6)
# print(ret)

# 4.列表生成式
# val = [lambda:x for x in range(10)]
# ret = val[3]()
# print(ret)

