#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang


from random import randint
import time

def range_time(li,iter_type):
    start_time = time.time()
    if iter_type == 'range':
        for j in range(10000):
            for i in range(len(li)):
                pass
    elif iter_type == 'enumerate':
        for j in range(10000):
            for i,val in enumerate(li):
                pass
    stop_time = time.time()
    duration = stop_time - start_time
    print('range_time is:{} and the iterate type is:{}'.format(duration,iter_type))


li = [randint(0,10000) for i in range(10000)]
# print('li is:{}'.format(li))
range_time(li,'range')
range_time(li,'enumerate')