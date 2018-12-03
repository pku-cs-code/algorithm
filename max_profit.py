#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum=0
        li=[]
        flag=0
        temp=0
        if len(prices)==0 or len(prices)==1:
            return 1
        else:
            for index,val in enumerate(prices):
                if index==0:temp=prices[1]
                if index < len(prices) - 1:
                    if prices[index] < temp:
                        temp=prices[index+1]
                        li.append('')
                        li[flag]=temp
                    else:
                        flag += 1
                        li.append('')
                        li[flag]=temp
        print('li is:{}'.format(li))

# prices=[7,1,5,3,6,4]
prices=[1,2,3,4,5]
Solution().maxProfit(prices)