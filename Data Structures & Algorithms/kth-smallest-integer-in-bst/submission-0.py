# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    result: int
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.helper(root, k)
        return self.result
    
    def helper(self, root, k) -> int:
        # recursion O(n) root and k
        #base case 1: root == null
        if not root:
            return 0
        # recurse left and save return result
        left = self.helper(root.left, k)
        # recurse right
        right = self.helper(root.right, k - (left + 1))
        # if result == k - 1 save final result
        if left == k - 1:
            self.result = root.val
        # return left + right + 1
        return left + right + 1