#TC: O(n) 
#SC: O(1)
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = len(nums)-1 # setting d to length of nums-1

        for i in range(len(nums)-2,-1,-1): #run until the length of nums in reverse order
            if i + nums[i] >=d: # if d is lesser than or equal to i+nums[i]
                d = i # assign i to d

        return d == 0 # return true if i is equal to 0
