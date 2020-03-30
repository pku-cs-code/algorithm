#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang


class fn():
    def __init__(self):
        self.i = 0

    def __next__(self,n):
        # for i in range(10):
        self.i += 1
        print("before:{}".format(self.i))
        rev = yield n
        print("after:{}".format(self.i))
        print("rev:{}".format(rev))

f = fn()

f.__next__(1)
f.__next__(2)
f.__next__(3)
