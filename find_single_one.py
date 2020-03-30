#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang


class Solution:
    def singleNumber(self, nums) :
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                s.remove(nums[i])
            else:
                s.add(nums[i])
        else:
            for j in list(s):
                print(j)


Solution().singleNumber([2,2,1])