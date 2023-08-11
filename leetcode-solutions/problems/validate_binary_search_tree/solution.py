# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def bst(node, left, right):
            # A null node is a valid BST
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False
            
            # Both these must be true at all the times for the tree
            # to be a valid BST
            return bst(node.left, left, node.val) and \
            bst(node.right, node.val, right)
        
        return bst(root, float("-inf"), float("inf"))