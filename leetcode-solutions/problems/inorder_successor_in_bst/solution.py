# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        """
        # Generic solution - will work well for a normal binary tree
        # But for BST it can be optimized - check the next solution
        """
        self.result = None
        self.match = False

        def dfs(root, p):
            if not root:
                return
            
            dfs(root.left, p)

            if p.val == root.val:
                self.match = True

            if self.match:
                if root.val > p.val:
                    self.result = root
                    self.match = False
                    return
            
            dfs(root.right, p)
        
        dfs(root, p)
        return self.result

        """
        # Take advantage of the BST property - eliminate half of the solution space every every move
        successor = None

        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor
        """



                

        