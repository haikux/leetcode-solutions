# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        cnt = self.countUnivalSubtrees(root.left) + self.countUnivalSubtrees(root.right)
        if self.isSame(root):
            cnt += 1
        return cnt
        
    
    def isSame(self, node):
        if not node:
            return True
        if node.left and node.left.val != node.val:
            return False
        if node.right and node.right.val != node.val:
            return False

        if self.isSame(node.left) and self.isSame(node.right):
            return True
        else:
            return False
