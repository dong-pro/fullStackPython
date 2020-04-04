# print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2)

# luck = 88
# count = 1
# while count <= 3:
#     guess = int(input('输入你要猜的数：'))
#     if luck > guess:
#         if 3 - count == 0:
#             print('小了,没有机会了')
#         else:
#             print('小了,还有%s次机会' % (3 - count))
#     elif luck < guess:
#         if 3 - count == 0:
#             print('大了,没有机会了')
#         else:
#             print('大了,还有%s次机会' % (3 - count))
#     else:
#         print('牛逼克拉斯')
#         break
#     count += 1
# else:
#     print('Game Over!')

# count = 1
# while count <= 10:
#     if count == 7:
#         pass
#     else:
#         print(count)
#     count = count + 1

# count = 1
# while count <= 10:
#     if count == 7:
#         count = count + 1
#         continue
#     print(count)
#     count = count + 1

# count = 1
# sum = 0
# while count <= 100:
#     sum = sum + count  # 累加运算
#     count = count + 1
# print(sum)

# count = 1
# while count <= 100:
#     if count % 2 == 0:
#         print(count)
#     count = count + 1

# count = 1
# sum = 0
# while count <= 99:
#     if count % 2 == 1:  # 奇数
#         sum = sum + count
#     else:  # 偶数
#         sum = sum - count
#     count = count + 1
# print(sum)

# count = 1  # 尝试的次数
# while count <= 3:
#     username = input('请输入用户名:')
#     password = input('请输入密码:')
#     if username == 'admin' and password == '123':
#         print('恭喜你. 登录成功')
#         break
#     else:
#         print('对不起, 用户名或密码错误!')
#         print('还剩下%s次登录机会' % (3 - count))
#     count = count + 1

# str = input('请输入广告标语:')
# if '最' in str or '第一' in str or '国家级' in str or '稀缺' in str:
#     print('广告不合法. 把设计人拉出去毙了')
# else:
#     print('OK的')

# 质数
# n = int(input('请输入一个数:'))
# if n == 1:
#     print('不知道是不是')
# else:
#     count = 2
#     while count <= n - 1:  # 质数只能被1和自身整除. 让这个数从2开始除. 一直除到n-1 如果除开了 一定不是质数 到最后还没有除开. 一定是质数
#         if n % count == 0:
#             print('你这个不是质数')
#             break
#         count = count + 1
#     else:
#         print('是一个质数')