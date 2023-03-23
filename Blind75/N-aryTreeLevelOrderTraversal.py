class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root==None:  #  if no root node
            return [] # returning empty list
        
        q = deque() # creating queue 
        q.append(root)  # appending root to q
        result = []  # creating an empty list
        while q:  # run until q value
            size = len(q)  # getting len of queue
            level = []  # creating level empty array
            for i in range(size): 
                node = q.popleft()  # popping the value from queue and storing it in node
                level.append(node.val)  # appending the node value in level array
                
                for child in node.children:  # for every child in node of children
                    q.append(child)  # appending the child in the queue
                    
                    
            result.append(level)  # appending the level into the result array
            
        return result  # returning result