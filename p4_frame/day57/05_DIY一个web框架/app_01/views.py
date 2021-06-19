# -*- coding: UTF-8 -*-
# @Time: 2020-06-22 15:59
# @Author: wyd
# @File: views.py

import pymysql
from urllib.parse import parse_qs

def login(request):
    if request.get("REQUEST_METHOD") == "POST":
        try:
            request_body_size = int(request.get('CONTENT_LENGTH', 0))
        except ValueError:
            request_body_size = 0

        request_body = request['wsgi.input'].read(request_body_size)
        data = parse_qs(request_body)

        user = data.get(b"user")[0].decode("utf8")
        pwd = data.get(b"pwd")[0].decode("utf8")

        # 连接数据库
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='p2_web')  # db：库名
        # 创建游标
        cur = conn.cursor()
        SQL = "select * from userinfo WHERE NAME ='%s' AND PASSWORD ='%s'" % (user, pwd)
        cur.execute(SQL)

        if cur.fetchone():
            f = open("templates/backend.html", "rb")
            data = f.read()
            data = data.decode("utf8")
            return data.encode("utf8")
        else:
            print("OK456")
            return b"user or pwd is wrong"

    else:
        f = open("templates/login.html", "rb")
        data = f.read()
        f.close()
        return data
