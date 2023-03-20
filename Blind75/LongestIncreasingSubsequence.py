Tc:O(nlogn)
Sc:O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [] # creating the dp with empty array

        dp.append(nums[0]) # appending nums[0]
        for i in range(1,len(nums)): # run until the length of nums
            
            if dp[-1] < nums[i]: # if dp of last value is less than numsof i then append nums[i]
                dp.append(nums[i])
            else:
                index = self.binarySearch(dp,nums[i]) # calling the binarysearch with dp and nums[i]
                dp[index] = nums[i] # assigning the nums[i] to dp of index

            #print(dp)
        
        return len(dp) # returning the length of dp
    
    def binarySearch(self,dp,nums1):

        low = 0 # assigning the low to 0
        high = len(dp)-1 # assigning the high to length of dp

        while(low<=high): # run until low is less than high
            mid = low + (high-low) // 2 # finding the mid value
            if (dp[mid] == nums1): # if mid is equal to nums1 return mid
                return mid
            elif dp[mid] < nums1: # if mid is less than nums1 then move pointer to mid+1 else mid-1
                low = mid + 1
            else:
                high = mid - 1
            
        return low # return ing the low pointer
