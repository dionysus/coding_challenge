# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs(head: ListNode) -> ListNode:
    """

    >>> node01 = ListNode(1)
    >>> node02 = ListNode(2)
    >>> node03 = ListNode(3)
    >>> node04 = ListNode(4)
    >>> node01.next = node02
    >>> node02.next = node03
    >>> node03.next = node04
    >>> newList = swapPairs(node01)
    >>> newList.val
    2
    >>> newList.next.val
    1
    >>> newList.next.next.val
    4
    >>> newList.next.next.val
    3
    """
    # BASE CASE

    if head is None:
        return head

    if head.next is None:
        return head

    else:
        curr = head
        next = head.next

        head = head.next
        head.next = curr

        head.next.next = swapPairs(next.next)
        return head
