class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
       
        self.targetSum = targetSum # defining the targetsum
        self.result = [] # defining the empty array
        self.dfs(root,0,[]) # calling the dfs function with currsum and path 
        print(self.result) 
        return self.result # returning the result

    def dfs(self, root, currSum, path):
        if not root: # base condition
            return

        currSum += root.val # adding the root value with current sum
        path.append(root.val) # appending the root value in path

        self.dfs(root.left,currSum,path) # calling the dfs function recursively for left subtree

        if not root.right and not root.left: # if left and right is not present then targetsum is equal to current sum
            if self.targetSum == currSum:
                temp = path[:] # shallow copying
                self.result.append(temp) # appending the temp into the result

        self.dfs(root.right,currSum,path) # calling the dfs function recursively for right subtree
        
        path.pop() # backtracking 