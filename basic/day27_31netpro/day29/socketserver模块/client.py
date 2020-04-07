import socket

sk = socket.socket()

sk.connect(('127.0.0.1', 8899))

while 1:
    name = input(">>>>：")
    sk.send(name.encode('utf-8'))  # 字节

    response = sk.recv(1024)  # 字节
    print(response.decode('utf-8'))
