# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        # BFS - Level order traversal
        dq = deque()
        if root:
            dq.append(root)
        level = 0
        while dq:
            for _ in range(len(dq)):
                n = dq.popleft()
                if n.left:
                    dq.append(n.left)
                if n.right:
                    dq.append(n.right)
            level += 1
        
        return level
        """

        # DFS - recursive
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))