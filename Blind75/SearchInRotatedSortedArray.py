class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0 # assigning low in index 0
        high = len(nums) -1 # assigning high in last index
        
        while low<=high: # until low is lesser than high
            mid = low + (high - low) // 2 # finding mid value
            
            if nums[mid] == target: # if mid equals to target
                return mid
            if nums[low] <= nums[mid]: # if left is sorted
                if nums[low]<= target and target<nums[mid]: # if target is in range
                    high = mid-1
                else:
                    low = mid+1
            else: # if right is sorted
                if nums[mid]<target and target <= nums[high]: # if target is in range
                    low =mid+1
                else:
                    high=mid-1
        return -1
        