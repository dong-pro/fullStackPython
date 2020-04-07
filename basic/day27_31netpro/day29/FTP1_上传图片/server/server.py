# -*- coding:UTF-8 -*-
# @Time: 2019/9/26 9:35
# @Author: wyd
# @File: server.py

import socket
import json

# 创建连接
sock = socket.socket()
IP_PORT = ('127.0.0.1', 4444)
sock.bind(IP_PORT)
sock.listen(3)

# 等待客户端接入
while 1:
    print('server is working...')
    conn, addr = sock.accept()

    while 1:
        # 接收客户端发送的数据
        data = conn.recv(1024).decode('utf-8')
        print('file_info: ', data)  # {"action": "put", "filename": "111.jpg", "filesize": 93605}
        # 将接收到的数据格式从str转换成dict
        file_info = json.loads(data)
        # 获取其中的文件名和文件大小
        filename = file_info.get('filename')
        filesize = file_info.get('filesize')

        # 给客户端发送是否接收成功
        conn.send(b'200')

        #接收客户端发送的文件内容
        with open('put/'+filename, mode='wb') as f:
            # 设置计数器，和文件大小比较
            recv_data_length = 0
            # 循环，直到接收全部的文件数据
            while recv_data_length < filesize:
                data = conn.recv(1024)
                recv_data_length += len(data)
                f.write(data)
                print('文件总大小%s，已接收数据%s' % (filesize, recv_data_length))

                # 接收成功后给客户端发信息
                if recv_data_length == filesize:
                    conn.send(b'success')

        print('接收成功！')