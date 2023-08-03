# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0]

        self.dfs(root, result)
        return result[0]
    
    def dfs(self, node, result):
            if not node:
                return -1
            left = self.dfs(node.left, result)
            right = self.dfs(node.right, result)
            result[0] = max(result[0], 2 + left + right)
            return 1 + max(left, right)

    