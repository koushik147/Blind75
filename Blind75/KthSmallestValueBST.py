class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.result = 0 # assigning the result to 0
        self.k = k 
        self.inorder(root) # calling the dfs function with root
        return self.result # returnign the result

    def inorder(self, root):
        if not root or self.k <= 0: # base condition
            return

        self.inorder(root.left) # traversing the left side of root node
        self.k-=1 # decrementing the k value to match to 0
        if self.k == 0:
            self.result = root.val # if attains 0, then assign root value to result
        self.inorder(root.right) # traversing the left side of root node