# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        carry = 0
        dummy = ListNode(0)
        tail = dummy
        while l1 or l2 or carry:
            value1 = 0
            value2 = 0
            total = 0

            if l1 is not None:
                value1 = l1.val
                l1 = l1.next
            if l2 is not None:
                value2 = l2.val
                l2 = l2.next

            total = value1 + value2 + carry
            new_digit = total % 10
            carry = total // 10

            tail.next = ListNode(new_digit)
            tail = tail.next
        return dummy.next