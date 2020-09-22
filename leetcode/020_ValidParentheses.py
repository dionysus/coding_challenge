"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""

def isValid(s: str) -> bool:
    """
    >>> isValid('')
    True
    >>> isValid('()')
    True
    >>> isValid('[]')
    True
    >>> isValid('{}')
    True
    >>> isValid('{')
    False
    >>> isValid('(){}[]')
    True
    >>> isValid('({[]})')
    True
    >>> isValid('([{]})')
    False
    """

    tracker = []

    for char in s:
        if char == '(' or char == '{' or char == '[':
            tracker.append(char)
        else:
            if len(tracker) < 1:
                return False
            else:
                last = tracker.pop()

            if (char == ')' and last != '(') or \
                    (char == '}' and last != '{') or \
                    (char == ']' and last != '['):
                return False

    if len(tracker) > 0:
        return False
    else:
        return True
