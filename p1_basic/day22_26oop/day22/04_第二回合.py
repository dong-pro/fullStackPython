"""
完成以下功能:
    老狗/20岁/男/上山去砍柴
    老狗/20岁/男/开车去东北
    老狗/20岁/男/喜欢大宝剑
"""

# ##################### 函数版本 #########################
'''
def kc(name, age, gender):
    data = "%s,性别%s,今年%s岁,喜欢上山砍柴" % (name, gender, age)
    print(data)

def db(name, age, gender):
    data = "%s,性别%s,今年%s岁,喜欢开车去东北" % (name, gender, age)
    print(data)

def bj(name, age, gender):
    data = "%s,性别%s,今年%s岁,喜欢大宝剑" % (name, gender, age)
    print(data)

kc('老狗', 20, '男')
kc('老狗', 20, '男')
db('老狗', 20, '男')
bj('老狗', 20, '男')
'''
# ##################### 面向对象1 #########################
'''
class LaoGou:
    def __init__(self, name, age, gender):  # 特殊的方法,如果 类名() ,则该方法会被自动执行 (构造方法)
        self.n1 = name
        self.n2 = age
        self.n3 = gender

    def kc(self):
        data = "%s,性别%s,今年%s岁,喜欢上山砍柴" % (self.n1, self.n3, self.n2)
        print(data)

    def db(self):
        data = "%s,性别%s,今年%s岁,喜欢开车去东北" % (self.n1, self.n3, self.n2)
        print(data)

    def bj(self):
        data = "%s,性别%s,今年%s岁,喜欢大宝剑" % (self.n1, self.n3, self.n2)
        print(data)

obj = LaoGou('老狗', 20, '男')
obj.kc()
obj.db()
obj.bj()
'''


# ##################### 面向对象2 #########################
'''
class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.f = open(self.file_path, 'rb')

    def read_first(self):
        self.f.read()
        # ...
        pass

    def read_last(self):
        self.f.read()
        # ...
        pass

    def read_second(self):
        self.f.read()
        # ...
        pass

obj = FileHandler('C:/xx/xx.log')
obj.read_first()
obj.read_last()
obj.read_second()
obj.f.close()
'''

# def func(**kwargs):
#     print(kwargs['k1'])
#     print(kwargs['k2'])
#     print(kwargs['k6'])
#
# func(k1=123, k2=465, k6=9)

def new_func(arg):
    print(arg.k1)
    print(arg.k2)
    print(arg.k6)

class Foo:
    def __init__(self, k1, k2, k6):
        self.k1 = k1
        self.k2 = k2
        self.k6 = k6

obj = Foo(111, 22, 333)
print(obj)
new_func(obj)
