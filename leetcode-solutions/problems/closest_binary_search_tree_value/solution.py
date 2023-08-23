# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
        # Recursive solution
        
        self.minn = self.result = root.val

        def dfs(node, target):
            if not node:
                return None
            if (abs(node.val-target) < abs(target-self.minn)):
                self.minn = node.val
            elif (abs(node.val-target) == abs(target-self.minn)):
                if node.val < self.minn:
                    self.minn = node.val
            dfs(node.right, target)
            dfs(node.left, target)
        dfs(root, target)
        return self.minn
        """

        # Binary Search
        curr = root
        self.res = float("inf")
        while curr:
            if (abs(curr.val-target) < abs(self.res-target)):
                self.res = curr.val
            elif (abs(curr.val-target) == abs(self.res-target)):
                self.res = min(self.res, curr.val)
            if target < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return self.res




        