class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n = len(height)-1   # create n with the length of height-1
        first = 0   
        last = n    
        
        max_area = 0    
        
        while first <= last: # run until first is less than last
            max_area = max(max_area, (min(height[first],height[last])*(last-first))) # store the maximum between max_area and the minimum between height[first] and height[last] and multiply the difference between last and first
             
            if height[first] < height[last]: # if the height of first is less than the height of last
                first+=1 # increment first
            else:
                last-=1 # decrement last
                
                
        return max_area #Return the max_area