class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if not p and not q: # both p and q are null return true
            return True

        if not p or not q or p.val!=q.val: # if p or q is not equal and either of them return false
            return False

        if self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right): # check the left tree and right tree then return true
            return True