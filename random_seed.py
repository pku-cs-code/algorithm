#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang



from numpy import *
num=0
while(num<5):
    random.seed(5)
    # 如果这个值5选定了，那么代表生成的随机数不随机了。5代表随机数生成算法的开始的整数值
    print(random.random())
    num+=1

from numpy import *
num=0
random.seed(5)
while(num<5):
    print(random.random())
    num+=1