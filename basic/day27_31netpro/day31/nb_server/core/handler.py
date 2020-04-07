import os
import json
import socketserver
import shutil


class Action(object):
    def __init__(self):
        self.username = None

    def login(self, cmd_dict, conn):
        """
        登录逻辑
        :return:
        """
        self.username = 'wyd'

    def upload(self, cmd_dict, conn):
        """
        服务端完成上传文件（含断点续传）
        :param cmd_dict:
        :param conn:
        :return:
        """
        # 2. 获取文件信息
        file_md5 = cmd_dict['md5']
        file_name = cmd_dict['file_name']

        file_md5_path = os.path.join('home', self.username, file_md5)
        file_name_path = os.path.join('home', self.username, file_name)
        upload_file_size = cmd_dict['size']

        # 3. 判断文件是否存在
        exist = os.path.exists(file_md5_path)
        if not exist:  # 不续传
            # 3.1.1 可以开始上传了，我已经准备好。
            response = {'code': 1001}
            conn.sendall(json.dumps(response).encode('utf-8'))

            # 3.1.2 接收上传的文件内容
            f = open(file_md5_path, 'wb')
            recv_size = 0
            while recv_size < upload_file_size:
                data = conn.recv(1024)
                f.write(data)
                f.flush()
                recv_size += len(data)
            f.close()

            # 3.1.3 改名字
            shutil.move(file_md5_path, file_name_path)

        else:  # 续传
            # 3.2 续传+大小
            exist_size = os.stat(file_md5_path).st_size
            response = {'code': 1002, 'size': exist_size}
            conn.sendall(json.dumps(response).encode('utf-8'))

            f = open(file_md5_path, 'ab')
            recv_size = exist_size
            while recv_size < upload_file_size:
                data = conn.recv(1024)
                f.write(data)
                f.flush()
                recv_size += len(data)
            f.close()

            # 3.1.3 改名字
            shutil.move(file_md5_path, file_name_path)

    def downlowd(self):
        """
        下载逻辑
        :return:
        """
        pass


class NbServer(socketserver.BaseRequestHandler):
    def handle(self):
        """
        self.request 是客户端的socket对象
        :return:
        """
        # 1. 接收命令
        upload_cmd_bytes = self.request.recv(8096)
        cmd_dict = json.loads(upload_cmd_bytes.decode('utf-8'))
        action = Action()
        if action.username:  # 已登录
            action_name = cmd_dict['cmd']
            getattr(action, action_name)(cmd_dict, self.request)
        else:  # 未登录
            action.login(cmd_dict, self.request)


def run():
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8001), NbServer)
    server.serve_forever()
