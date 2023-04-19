#Time_Complexity: o(n)
#Space_Complexity: O(n)
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maximum = root.val # assign the root value in the maximum
        self.dfs(root) # calling the dfs function with root
        return self.maximum # returning the maximum


    def dfs(self,root):
        #base condition
        if not root:
            return 0

        # choose leftsum, Nochoose
        leftSum = max(self.dfs(root.left), 0)
        # choose rightSum, Nochoose
        rightSum = max(self.dfs(root.right),0)

        rootSum = leftSum + rightSum + root.val # adding the leftsum with rightsum and root value

        self.maximum = max(self.maximum, rootSum) # assigning the maximum between maximum and rootsum

        return max(leftSum, rightSum) + root.val # returning the root value with leftsum or rightsum
