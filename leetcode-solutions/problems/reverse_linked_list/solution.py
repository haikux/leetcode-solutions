# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Three pointer approach
        current = head
        prev = nxt = None

        while(current != None):
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        head = prev
        return head
        