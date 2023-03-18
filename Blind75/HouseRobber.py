#TC: O(n) 
#SC: O(1)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: # if length of nums is 1 return nums[0]
            return nums[0]
        if len(nums) == 2: # if length of nums is 2 return the max betwen nums[0] and nums[1]
            return max(nums[0],nums[1])
        firstprev = nums[0] # assigning the first pointer to nums[0]
        secondprev = max(nums[0],nums[1]) # assigning the second pointer to max between the nums[0] nad nums[1]
        for i in range(2,len(nums)): #run until the length of nums from 2
            curr = max(secondprev,firstprev + nums[i]) # assigning the curr with the max value between second pointer and first pointer with nums[i]
            firstprev=secondprev # assigning the second pointer to first pointer
            secondprev=curr # assigning the curr to seconf pointer
        return curr # returning the curr pointer
