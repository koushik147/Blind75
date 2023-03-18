#TC: O(n) 
#SC: O(len(t))

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #low var as zero
        low=0
        #and high var to end
        high=len(s)-1

        #iterate until low is less than high
        while low<high:
            #if low is alphanumeric 
            if not s[low].isalnum():
                #move low to next
                low+=1
                #then continue
                continue
            # if high is alphanumeric
            if not s[high].isalnum():
                #high is decrement to one
                high-=1
                continue
            #convert the low and high is lower
            if s[low].lower()!=s[high].lower():
                return False
            #add low to one
            low+=1
            #decrement high minus one
            high-=1
        #if return true
        return True 
        
