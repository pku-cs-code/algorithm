#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang

import random

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        length = len(prices)
        prices.append(0)
        for i in range(length):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]
        return profit

prices=[random.randrange(10) for j in range(10)]


Solution().maxProfit(prices)