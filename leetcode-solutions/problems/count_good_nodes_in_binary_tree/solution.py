# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, float("-inf"))
    
    def dfs(self, root, max_val):
        if not root:
            return 0
        
        res = 1 if root.val >= max_val else 0
        max_val = max(root.val, max_val)
        res += self.dfs(root.left, max_val)
        res += self.dfs(root.right, max_val)
        return res



