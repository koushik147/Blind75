#Time_Complexity: O(n)
#Space_Complexity: O(n)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: # base condition
            return []
        result = []
        q = deque() # creating a queue and appending the root
        q.append(root)
        
        while q: # run until the q present, with the size of q 
            size = len(q)
            level = []
            for i in range(size): # for the size of q, popleft the value and traverse through the left and right side side of binary tree
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            result.append(node.val) # appending the node value in the result
        return result # returning the result
