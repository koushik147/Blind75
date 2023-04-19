# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Time_Complexity: O(n)
#Space_Complexity: O(n)
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root: # if root not present then return empty list
            return []
        result = [[root.val]] # appending the root value to result
        q = deque() # creating the deque() and appending the root 
        q.append(root)
        while q:
            size = len(q) # assigning the size with length of q
            #create level list to add level wise processing
            level = []

            for _ in range(size):
                node  = q.popleft() # popping the left value in the queue
                
                if node.left: # if left node is present then append into queue and update in level list
                    q.append(node.left)
                    level.append(node.left.val)

                if node.right: # if right node is present then append into queue and update in level list
                    q.append(node.right)
                    level.append(node.right.val)
            if level: # if level is not empty then append level to result and return result
                result.append(level)

        return result
