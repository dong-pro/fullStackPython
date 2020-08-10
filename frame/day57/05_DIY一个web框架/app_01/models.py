# -*- coding: UTF-8 -*-
# @Time: 2020-06-22 15:58
# @Author: wyd
# @File: models.py

import pymysql

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='web')  # db：库名
# 创建游标
cur = conn.cursor()

sql = '''
create table userinfo(
        id INT PRIMARY KEY ,
        name VARCHAR(32) ,
        password VARCHAR(32)
)

'''

cur.execute(sql)

# 提交
conn.commit()
# 关闭指针对象
cur.close()
# 关闭连接对象
conn.close()
