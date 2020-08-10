# -*- coding: UTF-8 -*-
# @Time: 2020-06-22 14:37
# @Author: wyd
# @File: 03_httpdemo.py

import socket

sock = socket.socket()
sock.bind(("127.0.0.1", 8808))
sock.listen(5)

while 1:
    print("server waiting.....")
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print("data", data)

    # 读取html文件
    with open("login.html", "rb") as f:
        data = f.read()

    conn.send((b"HTTP/1.1 200 OK\r\n\r\n%s" % data))
    conn.close()
