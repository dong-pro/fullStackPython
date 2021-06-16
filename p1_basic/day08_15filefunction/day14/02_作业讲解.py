# lst = ['kobe brant', 'anthony', 'sitannisilafu', '赵一宁', '峰哥', '石可心', '吴彦祖', '山本五十六', '松下索尼阿玛尼']
# ll = [name.upper() for name in lst if len(name) > 3]
# print(ll)

# lst = [(i, n) for i in range(5) for n in range(5) if i % 2 == 0 and n % 2 == 1]
# print(lst)

# M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([i[2] for i in M])
# # [3, 6, 9]
# print([[i-2, i-1, i-0] for i in [3, 6, 9]])

# (4)求出50以内能被3整除的数的平方，并放入到一个列表中。
# print([i**2 for i in range(50) if i % 3 == 0])

# 6.
# print([(i, i + 1) for i in range(6)])

# 7.
# lst = ['admin', 'root', '老男孩', '太白']
# print([el+str(index) for index, el in enumerate(lst)])
# print([lst[i] + str(i) for i in range(len(lst))])

# x = {
#     'name': 'admin',
#     'Values': [{'timestamp': 1517991992.94,
#                 'values': 100, },
#                {'timestamp': 1517992000.94,
#                 'values': 200, },
#                {'timestamp': 1517992014.94,
#                 'values': 300, },
#                {'timestamp': 1517992744.94,
#                 'values': 350},
#                {'timestamp': 1517992800.94,
#                 'values': 280}
#                ], }
#
# lst = [[el['timestamp'], el['values']] for el in x['Values']]
# print(lst)