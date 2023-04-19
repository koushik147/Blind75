#Time_Complexity: o(n)
#Space_Complexity: O(n)
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = [] # creating a empty result

        if not root:
            return []

        q = deque() # creating a deque and appending the root        
        q.append(root)

        while q:
            level = [] # for the lenght of q popleft the queue and store it in node
            size = len(q)
            for i in range(size):
                node = q.popleft()
                level.append(node.val) # adding the node's value in the level list
                if node.left:
                    q.append(node.left) # traversing to the left node
                if node.right:
                    q.append(node.right) # traversing to the right node

            if len(result) % 2 != 0: # if the length of the present result list is odd, then reverse the level list
                level = level[::-1]

            result.append(level) # append the level array to the result array, then return the result
        return result
