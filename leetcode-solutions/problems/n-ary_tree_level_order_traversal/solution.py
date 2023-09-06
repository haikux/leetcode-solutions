"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q = deque()
        if root:
            q.append(root)
        
        result = []
        while q:
            tmp = []
            for _ in range(len(q)):
                n = q.popleft()
                tmp.append(n.val)
                for c in n.children:
                    q.append(c)
            result.append(tmp)
        return result
        