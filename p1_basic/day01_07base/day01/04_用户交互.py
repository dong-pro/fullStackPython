# 语法: 变量 = input('提示语')
content = input('你吃了么?')
print('我们在控制台接收到了:' + content)

# 让用户输入a, 让用户输入b. 计算机计算a+b的结果
a = input('请输入a:')  # input收到的内容是str
b = input('请输入b:')  # input收到的内容是str
c = int(a) + int(b)   # 将字符串转换成整数  int(字符串)
print(c)
