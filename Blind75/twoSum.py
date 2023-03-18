class Solution(object):
    def twoSum(self, nums, target): 
        comb = [] # creating a empty array
        for i in range(len(nums)): # run until length of nums
            for k in range(i+1,len(nums)):
                if (nums[i] + nums[k]) == target: # if adding nums[i] and nums[k] to target
                    comb.extend((i,k)) # then extend it to array
        return comb # returning array