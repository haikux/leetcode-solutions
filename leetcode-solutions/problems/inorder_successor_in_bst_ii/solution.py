"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right:
            left = node.right
            while left.left:
                left = left.left
            return left
            
        while node.parent and node.parent.right == node: 
            node = node.parent
        return node.parent

        
            
        