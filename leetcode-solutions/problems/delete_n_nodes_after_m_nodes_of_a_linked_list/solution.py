# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        # base case
        if head is None or head.next is None:
            return head
    
        prev = None
        curr = head

        while curr:
            for i in range(m):
                prev = curr
                curr = curr.next
                if not curr:
                    return head
        
            for i in range(n):
                if curr:
                    curr = curr.next
        
            prev.next = curr
        
            
    
        return head
                
