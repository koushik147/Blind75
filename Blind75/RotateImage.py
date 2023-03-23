class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) # assigning the length of matrix 
        #reverse the matrix
        l = 0
        r = n-1
        while l<r: # run until l is less than r
            matrix[l],matrix[r] = matrix[r],matrix[l] # swapping the l and r of matrix
            l+=1 # incrementing the l pointer to 1
            r-=1 # decrementing the r pointer to 1

        # now swap the elements diagonally across bottom left to top right
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j] # swapping the matrix of i,j to matrix of j,i