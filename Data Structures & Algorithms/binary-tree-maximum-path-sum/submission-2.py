# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = -2000 
        def dfs(node) -> int:
            nonlocal result
            # recursion O(n) state is curr node
            # base case 1: null
            if not node:
                return 0
            # recursive steps: check left and right
            left = dfs(node.left)
            right = dfs(node.right)
            print(result, left + right + node.val)
            result = max(result, left + right + node.val, node.val, left + node.val, right + node.val)
            # return max path value left + node val, right + node val, node val
            return max(left + node.val, right +node.val, node.val)
        dfs(root)
        return result
        