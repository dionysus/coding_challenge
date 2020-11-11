'''
21. Merge Two Sorted Lists
Difficulty: Easy
URL: https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(self, l1, l2):
    if l1 is None:
        return l2

    elif l2 is None:
        return l1

    elif l1.val <= l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1

    else:
        l2.next = mergeTwoLists(l2.next, l1)
        return l2
