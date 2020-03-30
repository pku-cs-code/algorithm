#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang


class Solution:
    def sortArray(self, nums):
        length  = len(nums)
        for i in range(length-1):
            # value = nums[i]
            for j in range(i+1,0,-1):
                # print("j is:{}".format(j))
                if nums[j] < nums[j-1]:
                    temp = nums[j]
                    nums[j] = nums[j-1]
                    nums[j-1] = temp

        else:
            return nums

import  random
li = [   random.randrange(10000)  for j in range(100)  for i in range(10) ]
print(li.__len__())
print(Solution().sortArray(li))
