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
            idx=0
            nums[idx]=nums[0]
            for index,val in enumerate(nums):
                if val != nums[idx]:
                    idx += 1
                    nums[idx]=val
            return idx+1