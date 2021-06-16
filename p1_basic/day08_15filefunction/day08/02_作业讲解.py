# num = input('请输入一个三位数:')
# # s = 0
# # for c in num:
# #     s = int(c) ** 3 + s
# s = int(num[0]) ** 3 + int(num[1]) ** 3 + int(num[2]) ** 3
#
# if int(num) == s:
#     print(num, '是水仙花数')
# else:
#     print('不是')
#
# for c in range(100, 1000):
#     baiwei = c // 100
#     shiwei = c % 100 // 10
#     gewei = c - baiwei * 100 - shiwei * 10
#     if c == (baiwei ** 3 + shiwei ** 3 + gewei ** 3):
#         print(c)

# from random import randint
#
# s = set()
# while len(s) < 7:
#     r = randint(1, 36)
#     s.add(r)
# print(s)

# salary = int(input('请输入你的工资:'))
# if salary <= 2000:
#     print('没税')
# elif salary <= 4000:
#     print('有税')
#     print((salary - 2000) * 0.03)
# elif salary <= 6000:
#     print(2000 * 0.03 + (salary - 4000) * 0.05)


'''
2. 给出一个纯数字列表. 请对列表进行排序(升级题).
思路:
1. 完成a和b的数据交换. 例如, a = 10, b = 24 交换之后, a = 24, b = 10
2. 循环列表. 判断a[i]和a[i+1]之间的大小关系, 如果a[i]比a[i+1]大. 则进行互换. 循环结束的时候. 当前列表中最大的数据就会被移动到最右端.
3. 想一想, 如果再次执行一次上面的操作. 最终第二大的数据就移动到了右端. 以此类推. 如果反复的进行执行相应的操作. 那这个列表就变成了一个有序列表.
'''

# 这个算法可以进行优化.在外层循环时条件改成len(lst) - count
# 冒泡排序,
lst = [5, 1, 7, 2, 6, 4, 5, 6]
count = 0
while count < len(lst) - count:  # 控制次数
    i = 0
    while i < len(lst) - 1:
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
        i = i + 1
    count = count + 1
    print(count)  # 查看循环次数，验证优化效果。
print(lst)

# lst.sort()
# print(lst)

# 交换
# abcdefg = 10
# baddfad = 5
# abcdefg,baddfad = baddfad,abcdefg
# # c = a
# # a = b
# # b = c
# print(abcdefg, baddfad)