# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isChildValid(root, float('-inf'), float('inf'))
    
    def isChildValid(self, root, minimum, maximum) -> bool:
        # recursion O(n) state root, min, max
        # base case 1: root is null
        if not root:
            return True
        # base case 2: root < min and > max
        if root.val >= maximum or root.val <= minimum:
            return False
        # recursive step 1: left child
            # set new max to current value
        # recursive step 2: right child
            # set new min to current value
        return self.isChildValid(root.left, minimum, root.val) and self.isChildValid(root.right, root.val, maximum)
        