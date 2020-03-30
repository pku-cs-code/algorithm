#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lenth = len(nums) - 1
        if lenth < 1 or k < 1:
            print("Input list is less than 2 no need to rotate, or num k is invalid")
            return

        if (k < lenth):
            nums.reverse()
            print('nums is:{}'.format(nums))
            print('nums[0:k] is:{}'.format(nums[0:k]))
            print('nums[k:] is:{}'.format(nums[k:]))
            nums[0:k] = reversed(nums[0:k])
            nums[k:] = reversed(nums[k:])
        else:
            for i in range (k):
                nums.insert(0, nums[lenth])
                del nums[lenth + 1]


        return nums

ls = [x for x in range(10)]
print(Solution().rotate(ls,3))
