import os

class ExistsError(Exception):
    pass

class KeyInvalidError(Exception):
    pass

def new_func(path, prev):
    """
    去path路径的文件中，找到前缀为prev的一行数据，获取数据并返回给调用者。
        1000,成功
        1001,文件不存在
        1002,关键字为空
        1003,未知错误
        ...
    :return:
    """
    response = {'code': 1000, 'data': None}
    try:
        if not os.path.exists(path):
            raise ExistsError()

        if not prev:
            raise KeyInvalidError()
        pass
    except ExistsError as e:
        response['code'] = 1001
        response['data'] = '文件不存在'
    except KeyInvalidError as e:
        response['code'] = 1002
        response['data'] = '关键字为空'
    except Exception as e:
        response['code'] = 1003
        response['data'] = '未知错误'
    return response


# def func(path, prev):
#     """
#     去path路径的文件中，找到前缀为prev的一行数据，获取数据并返回给调用者。
#         1000,成功
#         1001,文件不存在
#         1002,关键字为空
#         1003,未知错误
#         ...
#     :return:
#     """
#     response = {'code': 1000, 'data': None}
#     try:
#         if not os.path.exists(path):
#             response['code'] = 1001
#             response['data'] = '文件不存在'
#             return response
#         if not prev:
#             response['code'] = 1002
#             response['data'] = '关键字为空'
#             return response
#         pass
#     except Exception as e:
#         response['code'] = 1003
#         response['data'] = '未知错误'
#     return response

def show():
    return 8

def run():
    pass


# #############自定义异常############
# class MyException(Exception):
#     def __init__(self, code, msg):
#         self.code = code
#         self.msg = msg
# try:
#     raise MyException(1000, '操作异常')
#
# except MyException as obj:
#     print(obj.code, obj.msg)


# 知识点：如何自定义异常类？
class MyException(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

try:
    # 知识点：主动抛出异常
    raise MyException(1000, '操作异常')

except KeyError as obj:
    print(obj, 1111)
except MyException as obj:  # 知识点：捕获异常
    print(obj, 2222)
except Exception as obj:
    print(obj, 3333)