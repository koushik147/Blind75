class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #currentMinimum = [1]* len(nums)
        #currentMaximum = [1]* len(nums)
        currentMinimum = 1 # assigning the min pointer to 1
        currentMaximum = 1 # assigning the max pointer to 1
        globalMaximum = -10 # assigning the global max to -10

        start = 0 # starting pointer to 0
        end = 1 # ending pointer to 1

        for num in nums: # run until the nums in array calculate current maximum and current minimum 
            currentMinimum  = min(currentMinimum * num, currentMaximum * num, num) # getting min with current maximum with num 
            currentMaximum  = max(currentMinimum * num, currentMaximum * num, num) # getting max with current maximum with num
            
            if (currentMaximum[i] > globalMaximum): # maximum of ith value is greater than global max
                globalMaximum = currentMaximum[i] # assigning current maximum to global maximum
                end=i+1 # assigning end to i+1
                j=i # assigning i to j
                contributer = currentMaximum[j] # assigning current maximum to contributor
                while j>=0: # run until j is greater than 0
                    if nums[j]==0: # if nums of j is equal to 0 assign j to start and break the loop
                        start = j
                        break
                    else:
                        if contributer == nums[j]: # if contributor value equal to jth value then assign j to start pointer and break the loop
                            start = j 
                            break
                        contributer = contributer/nums[j] # assigning the contributor value by dividing the numsof i with contributor
                    j-=1
 
        prod = 1 # assigning the prod to 1
        for num in nums[start: end]: # run until the nums and slicing from start to end
            prod *=num # multiping prod with num and return the prod

        return prod 