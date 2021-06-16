# 将列表转换成字符串. 每个元素之间用_拼接
# s = '**'.join(['高华新', '刘清扬', '崔园樟'])
# print(s)
#
# ss = '高华新**刘清扬**崔园樟'
# ss.split('**')

# 字符串转换成列表: split()
# 把列表转换成字符串: join()

# s = '_'.join('马化腾')
# print(s)
#
# join(可迭代对象)

# lst = ['紫云', '大云', '玉溪', '紫钻','a','b']
# # lst.clear()
# new_lst = [] # 准备要删除的信息
# for el in lst: # 有一个变量来记录当前循环的位置
#     new_lst.append(el)
#
# # 循环新列表, 删除老列表
# for el in new_lst:
#     lst.remove(el)
#
# # 删除的时候, 发现. 剩余了以下内容. 原因是内部的索引在改变.
# # 需要把要删除的内容记录下来. 然后循环这个记录. 删除原来的列表
#
# print(lst)
# print(new_lst)


# lst = ['张国荣', '张铁林', '张国立', '张曼玉', '汪峰']
# # 删掉姓张的
# # 记录姓张的.
# zhangs = []
# for el in lst:
#     if el.startswith('张'):
#         zhangs.append(el)
# for el in zhangs:
#     lst.remove(el)
# print(lst)
# print(zhangs)

# 字典
# dic = {'提莫':'冯提莫', '发姐':'陈一发儿', '55开':'卢本伟'}
# # dic.clear()
# lst = []
# for k in dic:
#     lst.append(k)
#
# for el in lst:
#     dic.pop(el)
# print(dic)

# 综上. 列表和字典都不能在循环的时候进行删除. 字典在循环的时候不允许改变大小

# dic = {'apple':'苹果', 'banana':'香蕉'}
# # 返回新字典. 和原来的没关系
# ret = dic.fromkeys('orange', '橘子') # 直接用字典去访问fromkeys不会对字典产生影响
# ret = dict.fromkeys('abc',['哈哈','呵呵', '吼吼']) # fromkeys直接使用类名进行访问
# print(ret)
a = ['哈哈', '呵呵', '吼吼']
ret = dict.fromkeys('abc', a)  # fromkeys直接使用类名进行访问
a.append('嘻嘻')
print(ret)
