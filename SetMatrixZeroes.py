#Time_Complexity: O(mn)
#Space_Complexity: O(m+n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix) # assigning the length of matrix
        n = len(matrix[0]) # assigning the length of column
        
        rowSet = [False]*m # creating a rowset with values as false
        colSet = [False]*n # creating a colset with values as false

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0: # for every value in matrix '0' assign rowset and colset
                    rowSet[i] = True
                    colSet[j] = True

            if rowSet[i]: # if rowset is true then assign a empty matrix
                matrix[i] = [0] * n

        for i in range(m): # for every value in matrix changinf the column value as 0 if matches
            if rowSet[i]:
                continue
            for j in range(n):
                if colSet[j]:
                    matrix[i][j] = 0
