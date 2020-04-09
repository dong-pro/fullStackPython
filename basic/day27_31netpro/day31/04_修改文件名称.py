import os
import shutil

# py2 + win：报错
# os.rename('a.text','b.txt')

# py2+py3
shutil.move('c.txt', 'a.txt')

# 删除文件
# shutil.rmtree('D:\sylar\s15\day30')

# 类似微信中表情
v = '\ue056'
print(v)