class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        self.res = [] # craeting res empty array
        self.recur(root,0) # calling recur function recursively 
        return self.res # return res array
        
    def recur(self,root,count):
        
        if not root:
            return
        if count >= len(self.res): # if count is greater than length of res
            self.res.append(root.val) # appending root value in res
        
        self.recur(root.right,count+1) # calling recur function to the right subtree
        
        self.recur(root.left,count+1) # calling recur function to the left subtree