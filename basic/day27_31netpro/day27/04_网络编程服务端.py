import socket

# 创建服务端socket对象
server = socket.socket()

# 绑定IP和端口
server.bind(('127.0.0.1', 8000))

# 后边可以等5个人
server.listen(5)

print('服务端准备开始接收客户端的连接')
# 等待客户端来连接，如果没人来就傻傻的等待。
# conn是客户端和服务端连接的对象(伞)，服务端以后要通过该对象进行收发数据。
# addr是客户端的地址信息。
# #### 阻塞,只有有客户端进行连接，则获取客户端连接然后开始进行通信。
conn, addr = server.accept()

print('已经有人连接上了，客户端信息：', conn, addr)

# 通过对象去获取（王晓东通过伞给我发送的消息）
# 1024表示：服务端通过（伞）获取数据时，一次性最多拿1024字节。
data = conn.recv(1024)
print('已经有人发来消息了', data)

# 服务端通过连接对象（伞）给客户端回复了一个消息。
conn.send(b'stop')

# 与客户端断开连接（放开那把伞）
conn.close()

# 关闭服务端的服务
server.close()
