# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = j = head
        x = 0
        while j.next is not None:
            x += 1
            j = j.next
            if x > n:
                i = i.next

        if x < n:
            head = head.next
        else:
            i.next = i.next.next

        return head