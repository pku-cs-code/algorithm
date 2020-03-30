#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang


'''
ref blog:
https://blog.csdn.net/AlanGuoo/article/details/78006942

In [1]: class test1(object):
   ...:
   ...:     def __init__(self):
   ...:
   ...:         self.a = 1
   ...:         self.b = 2
   ...:
   ...:

In [2]: x=test1()

In [3]: x.__dict__
Out[3]: {'a': 1, 'b': 2}

In [4]: x.a
Out[4]: 1

In [6]: x.b
Out[6]: 2

In [7]: x.__dict__={'a':'a','b':'b'}

In [8]: x.a
Out[8]: 'a'

In [9]: x.b
Out[9]: 'b'

In [10]: x.__dict__={'a':'a','b':'b','c':'c'}

In [11]: x.b
Out[11]: 'b'

In [12]: x.c
Out[12]: 'c'


'''

class test(object):

    def __init(self):
        self.a=1
        self.b=2


ins = test()
print('ins.__dict__ is:',ins.__dict__)
