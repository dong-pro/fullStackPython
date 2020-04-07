# -*- coding:UTF-8 -*-
# @Time: 2019/9/26 9:35
# @Author: wyd
# @File: server.py

import socket
import json
import struct
import hashlib

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
        # 接收客户端发送的json的打包长度
        file_info_length_pack = conn.recv(4)
        file_info_length = struct.unpack('i', file_info_length_pack)[0]
        print(file_info_length)

        # 接收客户端发送的json字符串
        file_info_json = conn.recv(file_info_length).decode('utf-8')
        print('file_info: ', file_info_json)
        # 将接收到的数据格式从str转换成dict
        file_info = json.loads(file_info_json)

        # 获取其中的文件名和文件大小
        filename = file_info.get('filename')
        filesize = file_info.get('filesize')

        #循环接收客户端发送的文件内容
        md5 = hashlib.md5()
        with open('put/'+filename, mode='wb') as f:
            # 设置计数器，和文件大小比较
            recv_data_length = 0
            # 循环，直到接收全部的文件数据
            while recv_data_length < filesize:
                data = conn.recv(1024)
                recv_data_length += len(data)
                f.write(data)
                # MD5摘要
                md5.update(data)
                print('文件总大小:%s，已接收数据:%s' % (filesize, recv_data_length))

        print('接收成功！')

        # 给客户端发送接收完毕OK的信息
        conn.send(b'ok')
        print(md5.hexdigest())

        #接收客户端发送的加密文件，然后和服务端的加密文件比较，文件相同就发送203，不同发送204
        md5_client = conn.recv(1024).decode('utf-8')
        md5_server = md5.hexdigest()
        if md5_client == md5_server:
            conn.send(b'203')
        else:
            conn.send(b'204')