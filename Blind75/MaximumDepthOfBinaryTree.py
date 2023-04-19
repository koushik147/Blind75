#Time_Complexity: o(n)
#Space_Complexity: O(1)
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: # if root not present return 0
            return 0

        maxDepth = 0 # assigning the maxdepth to 0
        q = deque() # creating a queue and append the root
        q.append(root)

        while q:
            size = len(q) # creating the size with length of q
            maxDepth+=1 # incrementing the maxdepth with 1
            for _ in range(size): 
                node = q.popleft() # popping the left value in the queue

                if node.left: # if left node present then traverse to left node
                    q.append(node.left)

                if node.right: # if left node present then traverse to left node
                    q.append(node.right)

        return maxDepth # returing the maxdepth
