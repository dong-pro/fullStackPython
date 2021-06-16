import socket
import select


class Req(object):
    def __init__(self, sk, func):
        self.sock = sk
        self.func = func

    def fileno(self):
        return self.sock.fileno()


class Nb(object):

    def __init__(self):
        self.conn_list = []
        self.socket_list = []

    def add(self, url, func):
        client = socket.socket()
        client.setblocking(False)  # 非阻塞
        try:
            client.connect((url, 80))
        except BlockingIOError as e:
            pass
        obj = Req(client, func)
        self.conn_list.append(obj)
        self.socket_list.append(obj)

    def run(self):

        while True:
            rlist, wlist, elist = select.select(self.socket_list, self.conn_list, [], 0.005)
            # wlist中表示已经连接成功的req对象
            for sk in wlist:
                # 发生变换的req对象
                sk.sock.sendall(b'GET /s?wd=alex HTTP/1.0\r\nhost:www.baidu.com\r\n\r\n')
                self.conn_list.remove(sk)
            for sk in rlist:
                chunk_list = []
                while True:
                    try:
                        chunk = sk.sock.recv(8096)
                        if not chunk:
                            break
                        chunk_list.append(chunk)
                    except BlockingIOError as e:
                        break
                body = b''.join(chunk_list)
                # print(body.decode('utf-8'))
                sk.func(body)
                sk.sock.close()
                self.socket_list.remove(sk)
            if not self.socket_list:
                break
