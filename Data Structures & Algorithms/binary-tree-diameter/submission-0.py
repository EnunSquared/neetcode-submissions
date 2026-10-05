# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxDist = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(self, node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = dfs(self, node.left)
            right = dfs(self, node.right)
            self.maxDist = max(self.maxDist, left + right)
            return max(left , right) + 1

        dfs(self, root)
        return self.maxDist
        