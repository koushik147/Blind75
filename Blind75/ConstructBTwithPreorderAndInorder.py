class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: # if preorder and inorder is null return none
            return None

        root = TreeNode(preorder[0]) # assigning the preorder first value to root

        for i in range(len(inorder)): # for all elements in inorder 
            if inorder[i] == preorder[0]: # if inorder of i is equal to preorder of first value
                pivot = i # assign the index to pivot

        root.left = self.buildTree(preorder[1:pivot+1],inorder[:pivot]) # calling the function recursively for left of index in inorder and preorder
        root.right = self.buildTree(preorder[pivot+1:],inorder[pivot+1:]) # calling the function recursively for right of index in inorder and preorder

        return root # returning the root 