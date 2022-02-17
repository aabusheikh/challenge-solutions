# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        i = list1
        j = list2
        k = ListNode()
        list3 = k
        
        while i is not None and j is not None:
            if i.val < j.val:
                k.val = i.val
                i = i.next
            else:
                k.val = j.val
                j = j.next
            if i is not None or j is not None:
                k.next = ListNode()
                k = k.next
                
        while i is not None:
            k.val = i.val
            i = i.next
            if i is not None:
                k.next = ListNode()
                k = k.next

        while j is not None:
            k.val = j.val
            j = j.next
            if j is not None:
                k.next = ListNode()
                k = k.next

        return list3