# s = {"周杰伦", "的老婆", "叫昆凌", (1, 2, 3), "周杰伦"}
# lst = [11, 5, 4, 1, 2, 5, 4, 1, 25, 2, 1, 4, 5, 5]
# s = set(lst)  # 把列表转换成集合. 进行去重复
# lst = list(s)  # 把集合转换回列表.
# print(lst)

# 集合本身是可变的数据类型, 不可哈希, 有增删改查操作
s = {"刘嘉玲", '关之琳', "王祖贤"}
s.update("麻花藤")  # 迭代更新
print(s)

# 集合中的元素必须是可哈希的. 不重复的. 可以去重. 哈希hash算法
