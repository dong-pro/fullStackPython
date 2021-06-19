# -*- coding: UTF-8 -*-
# @Time: 2020-06-22 15:33
# @Author: wyd
# @File: 04_wsgiref_server.py

from wsgiref.simple_server import make_server

def application(environ, start_response):
    '''
    :param environ: 请求信息字典
    :param start_response: 封装响应格式的
    :return:
    '''
    print('environ', environ)
    print('PATH_INFO', environ.get('PATH_INFO'))
    start_response('200 OK', [('Content-Type', 'text/html'), ('k1', 'v1')])
    return [b'<h1>Hello, web!</h1>']

httpd = make_server('', 8080, application)

print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
