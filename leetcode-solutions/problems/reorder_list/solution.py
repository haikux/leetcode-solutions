# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Generate two lists
        # Reverse the second list
        # Merge two lists
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr1 = head
        curr2 = slow

        # Reverse second list
        prev = None
        while curr2:
            tmp = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = tmp
        
        curr2 = prev
        # Merging two lists
        while curr1 and curr2:
            tmp1, tmp2 = curr1.next, curr2.next
            curr1.next = curr2
            curr2.next = tmp1
            curr1, curr2  = tmp1, tmp2
            


