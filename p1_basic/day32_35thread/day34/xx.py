import multiprocessing
import time

def task(arg, dic):
    time.sleep(2)
    dic[arg] = 100

if __name__ == '__main__':
    m = multiprocessing.Manager()
    dic = {}

    process_list = []
    for i in range(10):
        p = multiprocessing.Process(target=task, args=(i, dic,))
        p.start()

    print('end')
