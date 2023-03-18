class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [[0 for i in range(amount+1)] for j in range(len(coins)+1)] # assigning the dp array with value 0
        
        for j in range(1,amount+1): # run until j and add 1 to dp[j] column
            dp[0][j] = amount+1
        
        for i in range(1,len(coins)+1): # run until the length of coins
            for j in range(amount+1): # run until the range of amount
                if j < coins[i-1]: # if j is less than i-1
                    dp[i][j] = dp[i-1][j] # assigning the previous row same column value to dp 
                else:
                    dp[i][j] = min(dp[i-1][j], 1+dp[i][j-coins[i-1]]) # assigning the minimum value between the previous row value and dp of jth-coins of previous value
                    
        if dp[-1][-1] == amount+1: # if last value of dp is equal to amount then return -1
            return -1
        return dp[-1][-1] # return the last value of dp