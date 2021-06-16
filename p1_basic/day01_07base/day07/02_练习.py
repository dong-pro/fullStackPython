# a = 128
# print(id(a))

# a = 'admin'  # 这是第一次产生admin
# b = 'admin'  # 这句话不会产生新的字符串
# print(id(a), id(b))

# a = '谦虚'
# b = '谦虚'
# lst = ['jj', 'jay', '谦虚']
# lst2 = ['jj', 'jay', '谦虚']
# print(id(lst), id(lst2))

# 在python中一般的字符串都是会被缓存的. 为了节约内存
# a = 'admin@root'
# b = 'admin@root'
# print(id(a), id(b))

# a = [1, 2, 3]
# b = a
# c = b
# # 列表的创建
# print(c == a)  # 判断的是值.
# print(c is a)  # 判断两个变量指向的是否是同一个对象

# s = '今天晚上约么?'
# bs = s.encode('utf-8')
# print(bs)

# ascii中的内容编码之后还是原来的内容
# 中文编码之后是\x

# bs = b'\xe4\xbb\x8a\xe5\xa4\xa9\xe6\x99\x9a\xe4\xb8\x8a\xe7\xba\xa6\xe4\xb9\x88?'  # 用什么编码就要用什么解码
# s = bs.decode('utf-8')
# print(s)

# gbk的一句话
bs = b'\xc4\xe3\xb3\xd4\xc1\xcb\xc3\xb4'
# 想要发给别人.
# 把这句话翻译成字符串
s = bs.decode('gbk')
bbs = s.encode('utf-8')
print(bbs)  # utf-8

a = [[11, 22, 33], [44, 55, 66]]
b = [[77, 88, 99], [88, 99, 10]]

f = zip(*a, *b)
print(list(f))