class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sets = set(nums) # creating a set of nums
        if len(nums) != len(sets): # if length of nums not equal to length of sets return True else False
            return True 
        else:
            return False