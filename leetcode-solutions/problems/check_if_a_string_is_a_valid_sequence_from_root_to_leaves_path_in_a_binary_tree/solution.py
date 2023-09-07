# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        if not root:
            return False

        def dfs(root, j):
            if not root or arr[j] != root.val:
                return False

            if j == len(arr) - 1:
                return (not root.left and not root.right)
            
            return dfs(root.left, j+1) or dfs(root.right, j+1)

        return dfs(root, 0)

            
            
        