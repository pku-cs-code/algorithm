#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang


# 迭代器
class yield_im(object):

    def __init__(self,start=0,stop=0):
        '''
        ref blog:
        http://www.codebelief.com/article/2017/02/python-advanced-programming-generator/

        生成器的工作方式与迭代器相同，可以被视为是迭代器的一种。需要注意的是，生成器只支持一遍的迭代。当一个生成器被迭代完之后，就无法再产生结果，此时必须使用一个新的生成器以便再次迭代。

        '''
        self.start = start
        self.stop = stop
    # def __doc__(self):
    #     pass

    def __iter__(self):
        return self

    def __next__(self):
        if (self.start < self.stop):
            start = self.start
            self.start += 1
            return start
        else:
            raise StopIteration

# 生成器
def zrange(start=0,stop=0):
    while start < stop:
        yield start
        start += 1
    # else:
    #     raise StopIteration

for i in zrange(0,9):
    print('yield num is:{}'.format(i))


# y = yield_im(1,9)
# print('y.__doc__ is.{}'.format(y.__doc__()))
#
# for i in range(8):
#     print('{} time next(y) is:{}'.format(i,next(y)))