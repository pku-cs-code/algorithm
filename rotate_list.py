#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        temp=[]
        for idx,val in enumerate(nums):
            if idx < len(nums) - k -1:
                temp=nums[idx:idx+4]