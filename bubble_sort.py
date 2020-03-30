#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang


import random

li = []
num = 1000

for i in range(num):
    li.append(random.randrange(1,num))

for k in range(len(li)-1):
    tmp = 0
    for l in range(0,len(li)-k-1):
        if li[l] > li[l+1]:
            tmp = li[l]
            li[l] = li[l+1]
            li[l+1] = tmp



for j in li:
    print(j)

