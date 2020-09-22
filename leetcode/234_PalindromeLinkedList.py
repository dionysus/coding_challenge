# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def isPalindrome(head: ListNode) -> bool:

    if head is None:
        return True

    start = head

    ListNode._prev = None

    while head.next is not None:
        head.next._prev = head
        head = head.next

    end = head

    while start is not None:
        if start.val != end.val:
            return False
        else:
            start = start.next
            end = end._prev

    return True
