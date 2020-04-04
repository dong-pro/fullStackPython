# 带w的.只要你操作了.就会清空源文件
# 如果文件不存在.会自动创建文件
# f = open('写文件01', mode='w', encoding='utf-8')
# f.write('天蓝蓝，水潺潺，一钩斜月晓天悬。\n')
# f.write('神仙若有怜人意，岂叫嫦娥居广寒。\n')
# f.flush()
# f.close()

# a模式
# 写的时候. 换行需要手动控制   \n
# f = open('写文件01', mode='a', encoding='utf-8')
# f.write('\n天若有情天亦老，月如无恨月常圆。\n')
# f.write('庄稼汉求下雨，渔夫要风好行船。')
# f.flush()
# f.close()

# # rb, wb, ab, bytes如果处理的是非文本文件, mode里如果有b. encoding就不能给了
# f = open('/Users/wangyadong/fullStackPython/basic/day08_15filefunction/day08/kkk.jpg', mode='rb')  # 这里不能写encoding
# e = open('/Users/wangyadong/fullStackPython/basic/day08_15filefunction/day08/abc/ff.jpg', mode='wb')
# for line in f:  # 从kkk图片读取 line你是不知道读取了多少数据的
#     e.write(line)  # 写入到文件夹abc下面
# f.close()
# e.flush()
# e.close()