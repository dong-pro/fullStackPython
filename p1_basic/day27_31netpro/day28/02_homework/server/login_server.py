import socket

sock = socket.socket()  # TCP协议
IP_PORT = ("127.0.0.1", 8899)
sock.bind(IP_PORT)
sock.listen(5)

while 1:
    conn, addr = sock.accept()
    while 1:
        try:
            data = conn.recv(1024).decode("utf8")
            print("接收信息：", data)
            print("接收信息：", type(data))
            print("-----", data.split("|"))
            user, pwd = data.strip().split("|")

            # 文件操作
            flag = False
            with open("account", "r") as f:

                for line in f:
                    print("===", line.strip().split(":"))
                    username, password = line.strip().split(":")
                    if username == user and password == pwd:
                        flag = True
                        break
            if flag:
                conn.send(b"success")
            else:
                conn.send(b"fail")
        except Exception as e:
            break