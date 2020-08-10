# -*- coding: UTF-8 -*-
# @Time: 2020-06-22 11:14
# @Author: wyd
# @File: 02_web本质.py

import socket

def handle_request(client):
    print(1111)
    request_data = client.recv(1024)
    print(2222)
    print("request_data: ", request_data)
    print(3333)

    client.send("HTTP/1.1 200 OK\r\nstatus: 200\r\nContent-Type:text/html\r\n\r\n".encode("utf8"))
    client.send("<h1>Hello, luffycity!</h1><img src=''>".encode("utf8"))
    print(4444)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8088))
    sock.listen(5)

    while True:
        print("the server is waiting for client-connection....")
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()


if __name__ == '__main__':
    main()
