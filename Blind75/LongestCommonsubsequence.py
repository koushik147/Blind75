class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1) # length of text1
        n = len(text2) # length of text2
        grid = [[0 for i in range(n+1)] for j in range(m+1)] # creating the grid value with 0

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1): # run until the loop reaches the last cell and check whether text1 is equal to text2 then add the grid [i][j] with 1
                if text1[i]==text2[j]:
                    grid[i][j] = 1+ grid[i+1][j+1]

                else:
                    grid[i][j] += max(grid[i][j+1],grid[i+1][j]) # assign the grid[i][j] with the maximum value between the grid[i+1][j] and grid[i][j+1]


        return grid[0][0] # return the grid starting value
        




