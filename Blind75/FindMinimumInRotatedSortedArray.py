class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0 # assigning l to index 0
        h = len(nums) - 1 # assigning h to last index
        
        if(nums[l]<=nums[h]): # if sorted
            return nums[l] # return first element in array
        
        while(l<=h): # until l less than h
            mid = l + (h-l) // 2 # finding mid value
            if (nums[mid]>nums[mid+1]): # if mid is greater than mid+1
                return nums[mid+1] 
            elif nums[l] <= nums[mid]: # if left side is sorted
                l = mid+1
            else: # if right side is sorted
                h = mid-1