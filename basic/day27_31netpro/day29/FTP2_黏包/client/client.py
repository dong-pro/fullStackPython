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
import struct
import hashlib

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

        # 将字典转换成字符串，再编码成字节串
        file_info_json = json.dumps(file_info).encode('utf-8')
        # 因为黏包，所以用struct获取打包长度
        # 发送的数据类似   '{.....}' 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        res = struct.pack('i', len(file_info_json))

        # 发送 file_info_json的打包长度
        sock.send(res)

        # 发送 file_info_json字节串
        sock.send(file_info_json)

        #发送 文件数据
        md5 = hashlib.md5()
        with open(filename, mode='rb') as f:
            for line in f:
                sock.send(line)
                md5.update(line)

        # 接收服务端返回数据，打印
        data = sock.recv(1024)
        print(data)
        print(md5.hexdigest())

        # 发送加密后的文件
        md5_c = md5.hexdigest()
        sock.send(md5_c.encode('utf-8'))

        # 接收服务端返回的状态码，判断文件上传成功还是失败
        coding = sock.recv(1024).decode('utf-8')
        if coding == '203':
            print('文件完整！')
        else:
            print('文件上传失败！')
    except Exception as e:
        print('命令有误，请重新输入：')
        continue

