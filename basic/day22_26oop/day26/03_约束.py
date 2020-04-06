# pip3 install djangorestframework  源码

# from rest_framework.authentication import SessionAuthentication  # 2
# from rest_framework.authentication import RemoteUserAuthentication  # 1
# from rest_framework.authentication import TokenAuthentication  # 4


# ###########基于人为来约束######################
class BaseMessage(object):
    def send(self, x1):
        """
        必须继承BaseMessage，然后其中必须编写send方法。用于完成具体业务逻辑。
        """
        raise NotImplementedError(".send() 必须被重写.")

class Email(BaseMessage):
    def send(self, x1):
        """
        必须继承BaseMessage，然后其中必须编写send方法。用于完成具体业务逻辑。
        """
        pass

obj = Email()
obj.send(1)


# #########抽象类和抽象方法约束###############
from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):  # 抽象类

    def f1(self):
        print(123)

    @abstractmethod
    def f2(self):  # 抽象方法
        pass

class Foo(Base):

    def f2(self):
        print(666)

obj = Foo()
obj.f2()