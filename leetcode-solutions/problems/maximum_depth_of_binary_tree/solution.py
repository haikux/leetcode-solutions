# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)
        level = 0
        while q:
            for i in range(len(q)):
                t = q.popleft()
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            level += 1
        return level