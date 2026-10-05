# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        #traverse through tree
        def dfs(node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
            # p or q == val
            if p.val == node.val or q.val == node.val:
                return node
            # p > val and q < val or (q > val and p < val)
            if (p.val > node.val and q.val < node.val) or (q.val > node.val and p.val < node.val):
                return node
            # p and q > val
            if p.val > node.val and q.val > node.val:
                return dfs(node.right, p, q)
            # q and q < val
            else:
                return dfs(node.left, p, q)
        return dfs(root, p , q)
        