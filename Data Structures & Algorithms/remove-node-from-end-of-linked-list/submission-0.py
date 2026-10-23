# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while fast is not None:
            prev = prev.next
            slow = slow.next
            fast = fast.next

        prev.next = slow.next

        return dummy.next