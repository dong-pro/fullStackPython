class A(object):
    pass

class B(A):
    pass

class C(B):
    pass

class D(object):
    pass

class E(D, C):
    pass

class F(object):
    pass

class G(F):
    pass

class H(C, G):
    pass

class Foo(E, H):
    pass

# print(E.__mro__)
# print(H.__mro__)
"""
L(Foo + L(E)  + L(H) )

L(E) = E,D,C,B,A,object
L(H) = H,C,B,A,G,F,object

Foo = (object) + (G,F,object)
Foo,E,D,H,C,B,A,G,F,object
"""
print(Foo.__mro__)
