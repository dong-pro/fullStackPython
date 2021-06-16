import threading

print('666')


def func(arg):
    print(arg)


t = threading.Thread(target=func, args=('kkk',))
t.start()

print('end')
