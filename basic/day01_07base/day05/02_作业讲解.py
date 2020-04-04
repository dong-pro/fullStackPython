lis = [2, 3, 'k', ['qwe', 20, ['k1', ['tt', 3, '1']], 89], 'ab', 'adv']

# lis[3][2][1][1] = '100'
# print(lis)
# lis[3][2][1][1] = str(lis[3][2][1][1] + 97)
# print(lis)

# li = ['admin', 'root', 'test']
#
# s = ''  # admin
# for i in li:
#     s = s + i + '_'  # adminroot
# print(s[:-1])

# li = ['admin', 'root', 'test', 'python', ]
#
# for i in range(len(li)):
#     print(i)

# li = []
# for i in range(101):
#     if i % 2 == 0:
#         li.append(i)
#
# print(li)

# for i in range(10, 0, -1):
#     print(i)

# count = 100
#
# while count > 0:
#     print(count)
#     count -= 1
# li = []
# for i in range(100, 9, -1):
#     if i % 2 == 0:
#         li.append(i)
#
# for el in li:
#     if el % 4 != 0:
#         li.remove(el)
# print(li)
# li = [1, 'admin', 3]
#
# print(li.index('admin'))
# li = []
# for i in range(1, 31):
#     li.append(i)
# new_li = []
#
# for el in li:
#     if el % 3 == 0:
#         li[li.index(el)] = '*'
# print(li)
#
# for el in li:
#     if el % 3 == 0:
#         el = '*'
#     new_li.append(el)
#
# print(new_li)

# li = ['Test ', 'admin  xC', 'AbC   ', 'egon', ' ri  MoDule', 'Hello', '  aqc']
#
# for i in li:
#     i = i.replace(' ', '')
#     if (i.startswith('a') or i.startswith('A')) and i.endswith('c'):
#         print(i)

# li = ['苍老师', '东京热', '武藤兰', '波多野结衣']
#
# str_input = input('请输入内容:')
#
# li2 = []
# for i in li:
#     if i in str_input:
#         str_input = str_input.replace(i, '*' * len(i))
# li2.append(str_input)
#
# print(li2)

# li = [1, 3, 4, 'admin', [3, 7, 8, 'Train'], 5, 'PyThon']
#
# for i in li:
#     if type(i) == list:
#         for el in i:
#             if type(el) == str:
#                 print(f'"{el.lower()}"')
#             else:
#                 print(el)
#     else:
#         if type(i) == str:
#             print(f'"{i.lower()}"')
#         else:
#             print(i)

# li = []
# while 1:
#     str_input = input('请输入你的姓名和分数(格式:张三_44),输入Q退出:')
#     if str_input.lower() == 'q':
#         break
#     else:
#         ret = str_input.split('_')
#         print(ret)
#         li.append(ret[1])
#
# sum_num = 0
# for i in li:
#     sum_num = sum_num + int(i)
# print(sum_num / len(li))