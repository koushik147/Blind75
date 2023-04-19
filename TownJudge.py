#Time_Complexity: O(n)
#Space_Complexity: O(n)
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        indegree = [0]*(n+1) # creating indegree array
        for person,trusted_person in trust:
            #indegree[person-1]-=1 # decrementing indegree person by 1
            indegree[person]-=1
            indegree[trusted_person]+=1 # incrementing trusted person by 1
            
        for i in range(1,n+1):
            if indegree[i] == n-1: # if indegree is equal to last value
                return i # return i+1
        return -1 # else return -1
