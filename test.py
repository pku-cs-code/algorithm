#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang


class A():
    def __init__(self):
        self.__pri = ""
        self.__priv__ = "dd"

class B(A):
    def __init__(self):
        self.__priv = ""
    pass



print(dir(A()))
print(dir(B()))