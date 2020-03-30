#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        if len(nums) <= 1:
            return False
        else:
            for i in range(0, len(nums)):
                print(s)
                if nums[i] in s:
                    return True
                else:
                    s.add(nums[i])

            else:
                return False

# li = [2,14,18,22,22]
li = [3,3]
res = Solution().containsDuplicate(li)
print(res)
