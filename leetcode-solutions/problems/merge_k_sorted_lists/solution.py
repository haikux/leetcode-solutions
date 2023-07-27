# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0:
            return None

        while (len(lists) > 1):
            mergedL = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                # if the next index is out of bound return None
                list2 = lists[i + 1] if (i + 1) < len(lists) else None 
                mergedL.append(self.merge2List(list1, list2))
            lists = mergedL
        return lists[0]

    
    def merge2List(self, list1, list2):
        dummy = ListNode()
        ptr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next
        
        if list1:
            ptr.next = list1
        if list2:
            ptr.next = list2

        return dummy.next