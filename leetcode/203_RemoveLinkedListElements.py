# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        if head is None:
            return head

        elif head.val != val:
            if head.next is None:
                return head

            head.next = self.removeElements(head.next, val)
            return head

        else:
            if head.next is None:
                return None
            head = self.removeElements(head.next, val)
            return head

    def removeElements2(self, head: ListNode, val: int) -> ListNode:

        if head is None:
            return head

        start = prev = ListNode(0)

        while head is not None:
            if head.val == val:
                head = head.next
            else:
                prev.next = head
                prev = head
                head = head.next

        prev.next = head

        return start.next


    def removeElements3(self, head: ListNode, val: int) -> ListNode:

        if head is None:
            return head

        start = prev = ListNode(0)

        while head is not None:
            if head.val == val:
                head = head.next
            else:
                prev.next = head
                prev = head
                head = head.next

        prev.next = head

        return start.next
