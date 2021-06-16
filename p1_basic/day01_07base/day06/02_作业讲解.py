# dic = {'name': 'admin', 'age': 18}
# for i in dic:
#     print(i)
#     print(dic[i])

# 有字符串 'k:1|k1:2|k2:3|k3:4' 处理成字典 {'k':1,'k1':2....}  (升级题)
# s = 'k:1|k1:2|k2:3|k3:4'
# new_li = s.split('|')
# dic = {}
# print(new_li)
# for i in new_li:
#     k, v = i.split(':')
#     dic[k] = int(v)
# print(dic)

'''
有如下值li= [11,22,33,44,55,66,77,88,99,90]，将所有大于66的值
保存至字典的第一个key中，将小于66的值保存至第二个key的值中。
即：{'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}
'''
# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# dic = {'k1': [], 'k2': []}
# for i in li:
#     if i == 66:
#         continue
#     elif i > 66:
#         # print(dic.setdefault('k1').append(i))
#         dic['k1'].append(i)
#     else:
#         dic.setdefault('k2').append(i)
#
# print(dic)

'''
1：页面显示 序号 + 商品名称 + 商品价格，如：
        1 电脑 1999 
        2 鼠标 10
        …
2：用户输入选择的商品序号，然后打印商品名称及商品价格
3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
4：用户输入Q或者q，退出程序。
'''
goods = [{'name': '电脑', 'price': 1999},
         {'name': '鼠标', 'price': 10},
         {'name': '游艇', 'price': 20},
         {'name': '美女', 'price': 998}, ]
# while 1:
#     for i in goods:
#         # good = i
#         print(goods.index(i) + 1, i['name'], i['price'])
#
#     str_input = input('请输入您要选着的商品序号,输入Q/q退出:')
#
#     if str_input.isdigit() and 0 < int(str_input) < len(goods):  #这个len(goods)应该是len(goods)+1
#         i_index = int(str_input) - 1
#         print(goods[i_index]['name'], goods[i_index]['price'])
#     elif str_input.upper() == 'Q':
#         break
#     else:
#         print('输入有误,请重新输入!')