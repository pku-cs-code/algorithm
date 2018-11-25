#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang


li=[1,-2,3,10,-4,7,2,-5]

max_sum=li[0]
li_temp=[]

for index,val in enumerate(li):
    for i in range(index+1):
        for j in range(i,len(li)):
            if i==j  and li[i] > max_sum:
                li_temp=list(li[i])
                max_sum = li[i]
            else:
                temp_sum = sum(li[i:j])
                if temp_sum > max_sum:
                    li_temp=li[i:j]
                    max_sum=temp_sum
else:
    print('sum is:{}'.format(max_sum))
    print('sub list is:{}'.format(li_temp))