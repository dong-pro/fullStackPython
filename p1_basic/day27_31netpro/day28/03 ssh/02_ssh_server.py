import socket
import subprocess

server = socket.socket()

server.bind(('127.0.0.1', 8008))

server.listen(5)

while 1:
    print('server is working.....')
    conn, addr = server.accept()
    # 字节类型
    while 1:
        # 针对window系统
        try:
            cmd = conn.recv(1024).decode('utf-8')  # 阻塞
            if cmd == b'exit':
                break
            # 执行客户端输入的终端命令
            res = subprocess.Popen(cmd,
                                   shell=True,
                                   stderr=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   )
            out = res.stdout.read()   # 字节串
            err = res.stderr.read()
            # 响应字节长度
            print('out响应长度', len(out))
            print('err响应长度', len(err))
            if err:
                import struct
                # i模式
                header_pack = struct.pack('i', len(err))
                conn.send(header_pack)
                conn.send(err)
            else:
                # 构建报头
                import struct

                header_pack = struct.pack('i', len(out))
                print('header_pack', header_pack)
                # # 发送报头， 数据的长度
                conn.send(header_pack)
                # conn.send(str(len(out)).encode('utf-8'))
                # 发送数据
                conn.send(out)

        except Exception as e:
            break

    conn.close()
