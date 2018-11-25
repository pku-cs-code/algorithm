#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            pre=cur=0
            #nums[pre]=nums[0]
            for i in range(len(nums)):
                if nums[pre]==nums[cur]:
                    cur += 1
                else:
                    pre +=1
                    nums[pre]=nums[cur]
                    cur += 1
            return pre + 1
        