# -*- coding:UTF-8 -*-
# @Time: 2019/9/26 9:37
# @Author: wyd
# @File: client.py

'''
功能：客户端输入上传文件命令，服务端接收该文件
'''

import socket
import os
import json

# 和服务端建立连接
sock = socket.socket()
IP_PORT = ('127.0.0.1', 4444)
sock.connect(IP_PORT)

while 1:
    try:
        # 在客户端输入命令
        cmd = input('请输入执行的命令：')

        # 切割命令,找到文件名和文件大小
        action, filename = cmd.strip().split(' ')
        filesize = os.path.getsize(filename)

        # 放到字典中
        file_info = {
            'action': action,
            'filename': filename,
            'filesize': filesize
        }

        # 将字典转换成字符串，再转换成字节串发送到服务端
        file_info_json = json.dumps(file_info).encode('utf-8')
        sock.send(file_info_json)

        # 接收服务端发送的状态码
        code = sock.recv(1024).decode('utf-8')
        print(code)

        # 如果服务端返回200，进行文件上传
        if code == '200':
            # 上传文件操作
            with open(filename, mode='rb') as f:
                for line in f:
                    sock.send(line)
        else:
            print('服务器异常！')

        # 接收服务端完成后返回的信息
        rec_data = sock.recv(1024).decode('utf-8')
        print(rec_data)
    except Exception as e:
        print('命令有误，请重新输入：')
        continue

