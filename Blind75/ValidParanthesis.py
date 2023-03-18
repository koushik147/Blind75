class Solution:
    def isValid(self, s: str) -> bool:

        #if the length of string is even return false as it wont be a palindrome
        if len(s)%2!=0:
            return False
#create hashmap with key as close bracket and value as open btracket
        hashmap= { '}':'{', ']':'[', ')':'('}
    #create a stack
        stack = []

        #iterate through the string
        for ch in s:
            #if character in hashmap
            if ch in hashmap:
                #if stack is there and stack of last element is equal to hashmap of key
                if stack and stack[-1]==hashmap[ch]:
                    #then pop it from the stack
                    stack.pop()
                else:
                    #else return false
                    return False
#if character is not in hashmap
            else:
        #add the value to the stack
                stack.append(ch)
#check true if stack length is 0 or else false
        return len(stack)==0