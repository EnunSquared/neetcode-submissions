# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        n = 0
        q.append((root, 0))
        ans = []
        while len(q) > 0:
            node, curr_level = q.popleft()
            if node:
                q.append((node.left, curr_level + 1))
                q.append((node.right, curr_level + 1))
                if curr_level >= n:
                    ans.append([])
                    n += 1
                ans[curr_level].append(node.val)
        return ans




        