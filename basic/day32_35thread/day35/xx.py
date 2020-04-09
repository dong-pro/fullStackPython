"""
v = [
    [11,22], # 每个都有一个append方法
    [22,33], # 每个都有一个append方法
    [33,44], # 每个都有一个append方法
]

for item in v:
    print(item.append)
"""


class Foo(object):
    def __init__(self, data):
        self.row = data

    def append(self, item):
        self.row.append(item)


v = [
    Foo([11, 22]),  # 每个都有一个append方法
    Foo([22, 33]),  # 每个都有一个append方法
    Foo([33, 44]),  # 每个都有一个append方法
]

for item in v:
    print(item.append)
