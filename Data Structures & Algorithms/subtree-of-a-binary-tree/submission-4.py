# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #recursion O(n)
        # base case 1: root and subroot both null
        if not root and not subRoot:
            return True
        # base case 2: if root or subroot is null 
        if not root or not subRoot:
            return False
        # recursive step 1: root != subroot
        if root.val != subRoot.val:
            # recurse with root change
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        # recursive step 2: subroot == root
        if root.val == subRoot.val:
            # check if full subroot tree matches root tree
            if(self.isMatch(root, subRoot)):
                return True
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isMatch(self, root, subRoot) -> bool:
        #recursion O(k)
        # base case 1: root and subroot both null
        if not root and not subRoot:
            return True
        # base case 2: if root or subroot is null
        if not root or not subRoot:
            return False
        # recursive step 1: root != subroot
        if root.val != subRoot.val:
            return False
        # recursive step 2: root == subroot
        if root.val == subRoot.val:
            #check if children match
            return self.isMatch(root.left, subRoot.left) and self.isMatch(root.right, subRoot.right)
        