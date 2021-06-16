print((1 + 3) * 5)
print((3))
tu = (3,)  # 元组中如果只有一个元素. 需要在括号里写一个,
print(type(tu))
tu2 = tuple()  # 空元组
print(type(tu2))

tu3 = ('人民币', '美元', '英镑', '欧元')
# tu3.append('哈哈')
# tu3[0] = '日元'  # 不允许修改
# del tu3[2]  # 删除也不行

print(tu3[2])  # 索引可以用
print(tu3[::2])

for el in tu3:
    print(el)

# 元组的第一层是不能进行赋值的.内部元素是没有要求
tu = (1, '哈喽', 'how are you?', 'admin', ['root'])
tu[3].upper()
print(tu[3].upper())
print(tu)