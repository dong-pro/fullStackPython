# class Foo(object):
#     def __init__(self):
#         pass
#
#     def start(self):
#         return 1
#
#     def end(self):
#         return 10
#
# obj = Foo()
# obj.start()
# obj.end()

# class Foo(object):
#     def __init__(self):
#         pass
#
#     @property
#     def start(self):
#         return 1
#
#     @property
#     def end(self):
#         return 10
#
#
# obj = Foo()
# print(obj.start)
# print(obj.end)

# 总结:
#     1. 编写时
#            - 方法上方写 @property
#            - 方法参数:只有一个self
#     2. 调用时:无需加括号  对象.方法
#     3. 应用场景: 对于简单的方法,当无需传参且有返回值时,可以使用 @property


class Student(object):
    def __init__(self, score=0):
        self._score = score

    @property
    def score(self):
        print("getting score")
        print(self._score)
        return self._score

    @score.setter
    def score(self, value):
        print("setting score")
        if not isinstance(value, int):
            raise ValueError("score must be an integer!")
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
        print(self._score)


s = Student(60)
s.score
print("=====================")
s.score = 88
s.score