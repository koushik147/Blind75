class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0 # craeting l pointer to 0
        r = 1 # craeting r pointer to 1
        maxProfit = 0 # setting max profit to 0

        while r<len(prices): # run until r is less than length of prices
            if prices[r] > prices[l]: # if "r" price is high than "l"
                maxProfit = max(maxProfit, (prices[r] - prices[l])) # calculating max profit by finding max between maxprofit and prices of r-l
            else:
                l = r # chaning r pointer to l
            r+=1 # incrementing r by 1
        return maxProfit # returning the max profit