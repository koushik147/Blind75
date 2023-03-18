#TC: O(n) 
#SC: O(1)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] # creating an array with value 1
        for i in range(1,len(nums)): # run until the length of nums
            result.append(nums[i-1]*result[-1]) # append the i-1 * result's last value into the array
        suffix_prod = 1 # assigning the suffix prod as 1
        for i in range(len(nums)-2,-1,-1): # run until the len of nums in reverse order
            result[i] = result[i] * nums[i+1] * suffix_prod # calculating the result value by multipling with i+1 th value and the sufiix prod
            suffix_prod *= nums[i+1] # multipling the suffix prod with nums[i+1]
        return result # returning the result
