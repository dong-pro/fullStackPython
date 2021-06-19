#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/6/5

import json
# 导入模块
from flask import Flask
from flask import request
from flask import Response

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
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

#创建实例化请求对象
app = Flask(__name__)
# 定义路由
@app.route("/")
# 路由对应的函数处理
def index():
    # 响应数据
    resp = Response("<h2>首页</h2>")
    # 允许所有跨域访问
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

# MTV
@app.route("/course")
def courses():
    sql = 'SELECT * FROM userinfo'
    cur.execute(sql)
    results = cur.fetchall()

    # 返回json序列化的数据
    resp = Response(json.dumps({
        "msg": results
    }))

    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

# 前端发送post请求
# 定义路由
@app.route("/create", methods=["post", ])
def create():
    print(request.form.get('name'))
    # 读取user.json中的原始的数据
    with open("user.json", "r") as f:
        # 将数据反序列化
        data = json.loads(f.read())

    # 将新数据添加到原始的数据中
    data.append({"name": request.form.get('name')})

    # 将此时最新的数据再次写入文件中
    with open("user.json", "w") as f:
        f.write(json.dumps(data))

    # 再次返回最新的数据 响应会前端
    resp = Response(json.dumps(data))

    resp.headers["Access-Control-Allow-Origin"] = "*"

    return resp

if __name__ == '__main__':

    app.run(host="localhost", port=8800, )