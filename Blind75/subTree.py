class Solution(object):
    def isSubtree(self, root, subroot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        self.flag = False
        self.dfs(root,subroot) # calling the dfs function  with root and subroot
        return self.flag # returning the flag

    def isSameTree(self,root,subroot):

        if not root and not subroot: # both root and subroot are null return true
            return True

        if not root or not subroot or root.val!=subroot.val: # if root or subroot is not equal and either of them return false
            return False

        if self.isSameTree(root.left,subroot.left) and self.isSameTree(root.right,subroot.right): # check the left tree and right tree then return true
            return True
            
    def dfs(self,root,subroot):

        if not root: # base case
            return 

        self.dfs(root.left,subroot) # traversing through the left subtree
        self.dfs(root.right,subroot) # traversing through the right subtree

        if not self.flag and root.val == subroot.val: # if flag equal to false and root values matches then call issameTree
            self.flag = self.isSameTree(root,subroot)
        #print(self.flag)
        return self.flag # then return flag