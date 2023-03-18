class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if the length of s and t is not equal 
        if len(s)!=len(t):
            return False
        #create a bucket of 26
        bucket=[0]*26

        #iterate through the string s
        for ch in s:
            #subtract the ASCII value of character with small "a" to find the actual value of charcater and add it to one
            bucket[ord(ch)-ord("a")]+=1
        #iterate through the string t
        for ch in t:
            #subtract the ASCII value of character with small "a" to find the actual value of charcater and decrement it to one
            bucket[ord(ch)-ord("a")]-=1
            #if the length ar eequal then it should be less than one i we had a invalid anagram
            if bucket[ord(ch)-ord('a')] < 0:
                #so return false
                return False
        #or else erturn true
        return True