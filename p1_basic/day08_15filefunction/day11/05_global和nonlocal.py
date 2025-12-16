# a = 10  # 全局变量本身就是不安全的, 不能随意修改, 闭包
# def func():
#     global a  # 1. 可以把全局中的内容引入到函数内部 , 2. 在全局创建一个变量
#     #a = 20
#     a += 10  # a = a+10
#     print(a)
#
# func()
# print(a)

# a = 10
# def outer():
#     def inner():  # 在inner中改变a的值
#         nonlocal a  # 寻找外层函数中离他最近的那个变量；报错！nonlocal 不能指向全局变量
#         a = 20
#     inner()
# outer()

def outer():
    # 外层嵌套作用域的变量
    count = 0
    def inner():
        # 声明：使用的 count 是外层嵌套函数的变量
        nonlocal count
        count += 1
        print(f"内层函数：{count}")
    inner()
    print(f"外层函数：{count}")

outer()
# 输出：
# 内层函数：1
# 外层函数：1

# a = 1
# def fun_1():
#     a = 2
#     def fun_2():
#         global a
#         a = 3
#         def fun_3():
#             a = 4
#             print(a)
#         print(a)
#         fun_3()
#         print(a)
#     print(a)
#     fun_2()
#     print(a)
#
# print(a)
# fun_1()
# print(a)
