#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang


def gen(stop):
    start = 0
    print('generator starts...')
    while start < stop:
        print('before is:{}'.format(start))
        yield start
        print('after is:{}'.format(start))
        start += 1
    print('generator stops')

#列表推导式的生成器写法
Ge=(x for x in range(3))
print('type of Ge is:{}'.format(Ge))

G =gen(3)
# print('G.next() is:',G.__next__())

print(G.__next__())
print('seperator..')
print(G.__next__())
print('seperator..')

print(G.__next__())
print('seperator..')

print(G.__next__())
print('seperator..')


