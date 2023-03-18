class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one = 1 # assinging one to 1
        two = 1 # assinging two to 2

        if n==1: # if only 1 number return 1
            return 1

        for i in range(2,n+1): # run until the range of n+1 from 2
            one, two = two, one+two # swapping the one and two with one+two

        return two # returning two