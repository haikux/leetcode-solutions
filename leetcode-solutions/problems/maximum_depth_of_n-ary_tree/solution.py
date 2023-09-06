"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        q = deque()
        if root:
            q.append(root)
        result = 0
        
        while q:
            for _ in range(len(q)):
                n = q.popleft()
                if n.children:
                    q.extend(n.children)
            result += 1
        return result