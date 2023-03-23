class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.li = [] # creating a list
        self.prev = float("-inf") # assigning the previous pointer to -infinity
        self.flag = True
        self.inorder(root) # passing the root to the dfs function
               
        return self.flag # returning the flag

    def inorder(self,root):
        if root==None or not self.flag: # base condition
            return

        self.inorder(root.left) # traversing to left node of tree 
        
        if root.val<=self.prev: # if root value id lesser than prev then assign prev to false
            self.flag = False
        self.prev = root.val # assigning the root value to previous

        self.inorder(root.right) # traversing to right node of tree 
        