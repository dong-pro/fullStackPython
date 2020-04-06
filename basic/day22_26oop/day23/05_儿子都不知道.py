# 无法访问:
# class Base(object):
#     __secret = "受贿"
#
# class Foo(Base):
#     def func(self):
#         print(self.__secret)
#         print(Foo.__secret)
#
# obj = Foo()
# obj.func()

# 可以访问:
class Base(object):
    __secret = "受贿"

    def zt(self):
        print(Base.__secret)

class Foo(Base):
    def func(self):
        print(self.__secret)
        print(Foo.__secret)

obj = Foo()
obj.zt()