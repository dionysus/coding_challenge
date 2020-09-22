"""
Given a sorted linked list, delete all duplicates such that each element appear
only once.
"""

# Definition for singly-linked list.
# class ListNode():
#      def __init__(self, x):
#          self.val = x
#          self.next = None


def deleteDuplicates(self, head: ListNode) -> ListNode:

    if head.next is None:
        return head

    start = curr = head

    while curr is not None:
        if curr.next is None:
            break
        elif curr.val == curr.next.val:
            curr.next = curr.next.next
        elif curr.val != curr.next.val:
            curr = curr.next

    return start
