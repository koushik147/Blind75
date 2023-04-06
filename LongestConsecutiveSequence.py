class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums) # creating a set of nums

        maxLength = 0

        for i in range(len(nums)): # for every previous value of i in nums not in numset
            if (nums[i] -1) not in numSet:
                length = 1 # assigning the length to 1
                while (nums[i] + length) in numSet: # run until the length + ith value in numset and incrementing by 1
                    length +=1
                maxLength = max(maxLength, length) # assigning the maxlength 

        
        return maxLength # returning the maxlength