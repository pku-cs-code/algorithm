#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang


import timeit
setup = """
import random
random.seed(1)
l = range(10000)
random.shuffle(l)
"""
run1 = """
sorted(l)
"""
run2 = """
sorted(l, reverse=True)
"""
n1 = timeit.timeit(run1, setup, number=10000)
n2 = timeit.timeit(run2, setup, number=10000)
print(n1, n2)
print ((n2/n1 - 1)*100,"%")