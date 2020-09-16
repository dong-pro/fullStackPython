import pymysql

# 建立连接
conn = pymysql.connect(
    host='localhost',
    user='root',
    password="",
    database='db13',
    port=3306,
    charset='utf8'
)
# 创建游标
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = 'select * from userinfo'
print(sql)

res = cur.execute(sql)
print(res)

result = cur.fetchone()
print(result)

# relative 相对于原来的位置 如果是正值向下移动，反之亦然
# cur.scroll(-1,mode='relative')

# 相对于起始位置
cur.scroll(2,mode='absolute')
result = cur.fetchone()
print(result)


# 游标关闭 连接关闭
cur.close()
conn.close()
