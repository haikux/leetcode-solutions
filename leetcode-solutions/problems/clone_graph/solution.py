"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone_map = {}

        def dfs(node):
            if not node:
                return None
            if node in clone_map:
                return clone_map[node]
            
            copy = Node(node.val)
            clone_map[node] = copy

            # Now, recursively clone all the neighbors
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy
        
        return dfs(node)