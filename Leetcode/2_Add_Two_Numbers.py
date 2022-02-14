# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        node3 = ListNode()
        result = node3
        carry = 0
        while True:
            val = 0
            if node1 is not None:
                val += node1.val
                node1 = node1.next
            if node2 is not None:
                val += node2.val
                node2 = node2.next
            if carry > 0:
                val += carry
            carry = val // 10
            val = val % 10
            
            node3.val = val
            if (node1 is None) and (node2 is None) and (carry == 0):
                break
            node3.next = ListNode()
            node3 = node3.next
        return result