import multiprocessing
import threading
import queue
import time

# ##################### 进程间的数据共享:multiprocessing.Queue #####################
# q = multiprocessing.Queue()
#
# def task(arg, q):
#     q.put(arg)
#
# def run():
#     for i in range(10):
#         p = multiprocessing.Process(target=task, args=(i, q,))
#         p.start()
#
#     while True:
#         v = q.get()
#         print(v)
#
# run()

# ##################### 进程间的数据共享:Manager #####################
# def task(arg, dic):
#     time.sleep(2)
#     dic[arg] = 100
#
# if __name__ == '__main__':
#     m = multiprocessing.Manager()
#     dic = m.dict()
#
#     process_list = []
#     for i in range(10):
#         p = multiprocessing.Process(target=task, args=(i, dic,))
#         p.start()
#
#         process_list.append(p)
#
#     while True:
#         count = 0
#         for p in process_list:
#             if not p.is_alive(): #是否还存活
#                 count += 1
#         if count == len(process_list):
#             break
#     print(dic)
# m = multiprocessing.Manager()  # linux和mac
# dic = m.dict()
#
# def task(arg):
#         dic[arg] = 100
#
# def run():
#     for i in range(10):
#         p = multiprocessing.Process(target=task, args=(i,))
#         p.start()
#
#     input('>>>')
#     print(dic.values())
#
# if __name__ == '__main__':
#         run()
# ##################### 进程间的数据依赖其他电脑 #####################
# def task(arg, dic):
#     pass
#
# if __name__ == '__main__':
#     while True:
#         # 连接上指定的服务器
#         # 去机器上获取url
#         url = 'adfasdf'
#         p = multiprocessing.Process(target=task, args=(url,))
#         p.start()
