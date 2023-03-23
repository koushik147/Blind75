class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        while root: # run until root is present 
            if p.val<root.val and q.val<root.val: # if both p and q is lesser than the root value then check on the left side of the root
                root = root.left

            elif p.val>root.val and q.val>root.val: # if both p and q is greater than the root value then check on the right side of the root
                root = root.right

            else:
                return root # else return the root 

        return root