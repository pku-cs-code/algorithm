#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang


class Solution:
    def intersect(self, nums1, nums2):
        dic1 = self.getkey(nums1)
        dic2 = self.getkey(nums2)

        dic_intersect  = {}
        for key in dic1:
            if key in dic2:
                if dic1[key] >= dic2[key]:
                    dic_intersect[key] = dic2[key]
                else:
                    dic_intersect[key] = dic1[key]
        li = []
        print("dic1:%s" %dic1)
        print("dic2:%s" %dic2)
        print("dic_intersect:%s" %dic_intersect)
        for key in dic_intersect:
            for i in range(dic_intersect[key]):
                li.append(key)
        else:
            return li

    def getkey(self,nums):
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        else:
            print("dic:{}".format(dic))
            return dic


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(Solution().intersect(nums1, nums2))
