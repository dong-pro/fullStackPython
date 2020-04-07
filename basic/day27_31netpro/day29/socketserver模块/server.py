import socketserver

# 必须继承socketserver.BaseRequestHandler
class Myserver(socketserver.BaseRequestHandler):
    def handle(self):  # 方法名必须要叫handle
        # 字节类型
        while 1:
            # 针对window系统
            try:
                print("等待信息")
                data = self.request.recv(1024)  # 阻塞
                # 针对linux
                if len(data) == 0:
                    break
                if data == b'exit':
                    break
                response = data + b'SB'
                self.request.send(response)
            except Exception as e:
                break

        self.request.close()


'''
1 创建socket对象
2 self.socket.bind()
3 self.socket.listen(5)
'''
# socketserver.ForkingUDPServer
server = socketserver.ThreadingTCPServer(('127.0.0.1', 8899), Myserver)

server.serve_forever()  # 相当于 coon,addr = sock.accept()
