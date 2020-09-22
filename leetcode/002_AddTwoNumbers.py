# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    >>> node01A = ListNode(9)
    >>> node01B = ListNode(9)
    >>> node01A.next = node01B
    >>> node02A = ListNode(9)
    >>> new_list = addTwoNumbers(node02A, node01A)
    >>> node01A.val
    8
    >>> node01A.next.val
    0
    >>> node01A.next.next.val
    1
    """
    if not l1 and not l2:
        return None

    else:
        if l1 and not l2:
            v = l1.val
        elif l2 and not l1:
            v = l2.val
            l1, l2 = l2, None
        else:
            v = l1.val + l2.val

        if v >= 10:
            v -= 10
            if l1.next is None:
                if l2 is None or l2.next is None:
                    l1.next = ListNode(1)
                else:
                    l2.next.val += 1
            else:
                l1.next.val += 1

        l1.val = v

        if not l2:
            l1.next = self.addTwoNumbers(l1.next, None)
        else:
            l1.next = self.addTwoNumbers(l1.next, l2.next)
            
        return l1
