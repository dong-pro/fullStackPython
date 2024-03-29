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

# result = cur.fetchone()
# print(result)

# result = cur.fetchmany(1)
# print(result)

results = cur.fetchall()
print(results)

# -3 -2 -1 0 1 2 3 4 5

# relative 相对于原来的位置 如果是正值向下移动，反之亦然
# cur.scroll(-1,mode='relative')

# 相对于起始位置
cur.scroll(2, mode='absolute')
result = cur.fetchone()
print(result)

# 增 删 改 一定要commit()
conn.commit()

# 游标关闭 连接关闭
cur.close()
conn.close()
