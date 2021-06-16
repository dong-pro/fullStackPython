import socket
import struct

sk = socket.socket()

sk.connect(('127.0.0.1', 8008))

while 1:
    cmd = input('请输入命令：')
    sk.send(cmd.encode('utf-8'))  # 字节
    if cmd == '':
        continue
    if cmd == 'exit':
        break

    # 接收数据的长度
    header_pack = sk.recv(4)
    data_length = struct.unpack('i', header_pack)[0]
    print('data_length', data_length)
    '''
    b'xxx/xxx/xxx/bbbbbbbbbbbbbbbbbbbbbbbbbbb'
    '''
    # 计数
    recv_data_length = 0
    recv_data = b''
    # 循环接收数据的长度，输出接收的数据
    while recv_data_length < data_length:
        data = sk.recv(1024)
        recv_data_length += len(data)  # 拼接收到的字符串
        recv_data += data  # 更新计数器

    print(recv_data.decode('utf-8'))

sk.close()