import socketserver

'''看socket源码'''
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        pass


server = socketserver.ThreadingTCPServer(('127.0.0.1', 8001,), MyServer)
server.serve_forever()
