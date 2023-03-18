class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)   # create n as length of nums
        triplets = []   # create an empty array
        nums.sort() # sort nums
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:  # if the i is greater than 0 and nums[i] is equal to nums[i-1]
                continue
                
            p1= i+1 # create p1 pointer to i+1
            p2= n-1 # create p2 pointer to n-1
            target = 0 - nums[i] # create target as the difference between 0 and nums[i]
            
            while p1< p2: # run until p1 is less than p2
                if nums[p1]+nums[p2] == target: # if nums[p1]+nums[p2] is equal to target 
                    result = [nums[i], nums[p1], nums[p2]] # store nums[i], nums[p1], nums[p2] into the array
                    triplets.append(result) 
                    while p1<p2 and nums[p1] == nums[p1+1]: # run until p1 is less than p2 and nums[p1] is equal to nums[p1+1]
                        p1+=1   # increment p1 by 1
                        
                    while p1<p2 and nums[p2] == nums[p2-1]: # run until p1 is less than p2 and nums[p2] is equal to nums[p2-1]
                        p2-=1   # decrement p2 by 1
                    p1+=1   # increment p1 by 1
                    p2-=1   # decrement p2 by 1
                else:    
                    if target < nums[p1]+nums[p2]: # if the target is less than nums[p1]+nums[p2]
                        p2-=1 # decrement p2 by 1
                        
                    else: 
                        p1+=1 # increment p1 by 1
                        
        return triplets  # return triplets