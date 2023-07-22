"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copymap = {None: None}
        curr = head
        while curr:
            copymap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            tmp = copymap[curr]
            tmp.next = copymap[curr.next]
            tmp.random = copymap[curr.random] 
            curr = curr.next
        
        return copymap[head]
        