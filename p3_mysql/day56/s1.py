import pymysql

username = input('请输入用户名：')
pwd = input('请输入密码：')

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
cur = conn.cursor()
sql = 'insert into userinfo(name,pwd) values (%s,%s)'
print(sql)

res = cur.execute(sql, [username, pwd])
print(res)

# 增 删 改 一定要commit()
conn.commit()

# 游标关闭 连接关闭
cur.close()
conn.close()
