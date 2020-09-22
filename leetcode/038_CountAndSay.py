def countAndSay(n: int) -> str:
    """
    >>> countAndSay(1)
    '1'
    >>> countAndSay(2)
    '11'
    >>> countAndSay(3)
    '21'
    >>> countAndSay(4)
    '1211'
    >>> countAndSay(5)
    '111221'
    """
    num = "1"
    for i in range(n - 1):
        num = nextStr(num)
    return num

def nextStr(num: str) -> str:
    """
    >>> nextStr('1')
    '11'
    >>> nextStr('11')
    '21'
    >>> nextStr('21')
    '1211'
    >>> nextStr('1211')
    '111221'
    """
    result = ""
    j = 0

    for i in range(len(num)):
        if num[i] != num[j]:
            result += str(i - j)
            result += num[j]
            j = i

        if i == len(num) - 1:
            result += str(i - j + 1)
            result += num[j]

    return result
