# -*- coding:UTF-8 -*-
# @Time: 2019/8/25 17:01
# @Author: wyd
# @File: day09

list3 = [
    {'name': 'admin', 'hobby': '抽烟'},
    {'name': 'admin', 'hobby': '喝酒'},
    {'name': 'admin', 'hobby': '烫头'},
    {'name': 'admin', 'hobby': 'Massage'},
    {'name': 'root', 'hobby': '喊麦'},
    {'name': 'root', 'hobby': '街舞'},
    {'name': 'taibai', 'hobby': '开车'},
    {'name': 'taibai', 'hobby': '嫂子'},
]
list4 = []

for ren in list3:  # {'name': 'admin', 'hobby': '抽烟'},
    for el in list4:
        if el['name'] == ren['name']:
            el['hobby_list'].append(ren['hobby'])
            break
    else:
        dic = {}
        dic['name'] = ren['name']
        dic['hobby_list'] = [ren['hobby']]
        list4.append(dic)  # 第一个人进去
print(list4)