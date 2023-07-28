# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
cur = head
        start = end = cur
        prev = None
        cnt = 0
        while cur:
            if cnt == k:
                prev = self.reverse(start, end, prev)
                print(start)
                print("\n")
                start = cur
                cnt = 0
            cur = cur.next
            end = cur
            cnt += 1
        return head


    
    def reverse(self, start, end, prev):
        prev = end
        curr, ahead = start, start
        while curr and curr != end:
            ahead = curr.next
            curr.next = prev
            prev = curr
            curr = ahead
        return prev
"""
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        grpPrev = dummy

        while True:
            kth = self.getKth(grpPrev, k)
            if not kth:
                break
            grpNext = kth.next

            #Reverse the list
            prev, curr = kth.next, grpPrev.next
            while curr != grpNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = grpPrev.next
            grpPrev.next = kth
            grpPrev = tmp
        return dummy.next

    
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
        