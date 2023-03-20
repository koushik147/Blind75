class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.house(nums[1:]),self.house(nums[:-1])) # returning the max between two array using slice operation
    
    def house(self, nums: List[int]) -> int:
        firstprev=0 # setting pointer to 0
        secondprev=0 # setting pointer to 0

        if len(nums) == 1: # if length of array is 1 then return nums[0]
            return nums[0]

        for i in range(len(nums)): # run until the length of nums
            maximum = max(nums[i]+firstprev,secondprev) # assign the max value between the nums value, firstprev and secondprev
            firstprev= secondprev # setting second pointer to first
            secondprev = maximum # setting maximum pointer to second
        return maximum # returning the maximum value