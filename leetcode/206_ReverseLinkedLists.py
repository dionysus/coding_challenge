# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        ListNode.prev = None

        while head.next is not None:
            head.next.prev = head
            head = head.next

        start = head

        while head is not None:
            head.next = head.prev
            head = head.prev

        return start

    def reverseList2(self, head: ListNode) -> ListNode:
        prev = None
        while head is not None:
            head.next, prev, head = prev, head, head.next
        return prev
