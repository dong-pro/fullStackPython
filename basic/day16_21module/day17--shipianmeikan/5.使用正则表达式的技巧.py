import re

# ret=re.findall(r"\d+","1-2*(60+(-40.35/5)-(-4*3))")
# 从"1-2*(60+(-40.35/5)-(-4*3))"中取整数
# ['1', '2', '60', '40', '35', '5', '4', '3']
# print(ret)

# 你要匹配的内容太没有特点了 容易和你不想匹配的内容混在一起
# 精准的取到整数 过滤掉小数

ret = re.findall(r"\d+\.\d+|\d+", "1-2*(60+(-40.35/5)-(-4*3))")
print(ret)
ret = re.findall(r"\d+\.\d+|(\d+)", "1-2*(60+(-40.35/5)-(-4*3))")
ret.remove('')
print(ret)

# 正则表达式如果写的足够好的话 能够最大限度的简化我们的操作

# 正则表达式到底重要到什么程度
# 掌握作业中的所有内容
# 能够看懂常用的正则表达式
# 并且能够做出一些公司特异性要求的修改
