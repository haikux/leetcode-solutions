# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        len_ll = 0
        curr = head
        while curr:
            len_ll += 1
            curr = curr.next
        
        if n == 1 and len_ll == 1:
            return
        cnt = len_ll - n

        prev = None
        curr = head
        c = 0

        if not head:
            return head.next

        if cnt == 0:
            return curr.next
        while curr:
            if c == cnt:
                prev.next = curr.next
            prev = curr
            curr = curr.next
            c += 1
        
        return head
        """

        slow = fast = head
        for _ in range(n):
            fast = fast.next
        
        if not fast:
            return head.next 

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head