def func():
    pass

class Foo(object):
    def __call__(self, *args, **kwargs):
        pass

    def func(self):
        pass

obj = Foo()

print(callable(func))
print(callable(Foo))
print(callable(obj))
print(callable(obj.func))
