# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: # base condition
            return ""

        result = [] # defining a array
        q = deque() # defining a queue and appending the root
        q.append(root)
        while q: # run until queue and if node present then append the left and right into queue
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                result.append(str(node.val)) # appending the node value into the result
            else:
                result.append("null") # if hits null then append the null in the result
        return ",".join(result) # then joining the result and return
             
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if not data: # base condition
            return None

        i = 0
        data = data.split(",") # spliting the input
        root = TreeNode(int(data[0])) # creating the root node with int value of start
        i+=1
        q = deque() # creating the queue and appending the root
        q.append(root)

        while q: # run until the queue and pop the node's value
            curr = q.popleft()

            if data[i]!="null": # if not null then creating a tree node with value 
                curr.left = TreeNode(int(data[i]))
                q.append(curr.left) # appending the left value to queue
            i+=1

            
            if data[i]!="null": # if not null then creating a tree node with value 
                curr.right = TreeNode(int(data[i]))
                q.append(curr.right) # appending the right value to queue
            i+=1

        return root # returning the root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans