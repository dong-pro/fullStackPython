import socket

server = socket.socket()

server.bind(('127.0.0.1', 8001))

server.listen(5)
'''
了解2个while的作用；
为什么加try异常处理：
    客户端强制关闭连接，data = conn.recv(1024)  监听的套接字对象conn断开连接：
        针对Windows系统：异常报错
        针对Linux：接收一个空的data
'''
while 1:  # 服务端一直等待客户端连接
    print('server is working...')
    conn, addr = server.accept()
    # 字节类型
    while 1:  # 循环接收客户端发送的数据
        try:  # 针对Windows
            data = conn.recv(1024)  # 阻塞
            '''
            针对Linux
            if len(data)==0:
                break
            '''
            if data == b'exit':
                break
            response = data + b' SB'
            conn.send(response)
        except Exception as e:
            break
    conn.close()
