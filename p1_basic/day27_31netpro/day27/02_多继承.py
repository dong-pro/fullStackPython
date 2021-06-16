class A(object):
    pass

class B(object):
    def f1(self):
        print('B')

class C(A, B):
    pass

obj = C()

obj.f1()