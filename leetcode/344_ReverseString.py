from typing import List

def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.

    >>> s = list('hello')
    >>> reverseString(s)
    >>> s
    ['o', 'l', 'l', 'e', 'h']
    """
    if len(s) < 2:
        pass

    for i in range((len(s) // 2)):
        s[i], s[-(i+1)] = s[-(i+1)], s[i]

def reverseString_recur(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.

    >>> s = list('hello')
    >>> reverseString_recur(s)
    >>> s
    ['o', 'l', 'l', 'e', 'h']
    """

    if len(s) < 2:
        pass

    else:

        right_start = left_end = len(s) // 2

        if len(s) % 2 == 1:
            right_start += 1

        left = s[:left_end]
        right = s[right_start:]

        reverseString_recur(right)
        reverseString_recur(left)

        s[:left_end] = right
        s[right_start:] = left
