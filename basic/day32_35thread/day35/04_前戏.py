import socket

client = socket.socket()
client.setblocking(False)  # 将原来阻塞的位置变成非阻塞（报错）
# 百度创建连接: 阻塞

try:
    client.connect(('www.baidu.com', 80))  # 执行了但报错了
except BlockingIOError as e:
    pass

# 检测到已经连接成功

# 问百度我要什么？
client.sendall(b'GET /s?wd=alex HTTP/1.0\r\nhost:www.baidu.com\r\n\r\n')

# 我等着接收百度给我的回复
chunk_list = []
while True:
    chunk = client.recv(8096)  # 将原来阻塞的位置变成非阻塞（报错）
    if not chunk:
        break
    chunk_list.append(chunk)

body = b''.join(chunk_list)
print(body.decode('utf-8'))
