def strStr(haystack: str, needle: str) -> int:
    """
    Return the index of the first occurrence of needle in haystack,
    or -1 if needle is not part of haystack, or 0 if needle is an
    empty string.

    >>> strStr("hello", "ll")
    2
    >>> strStr("aaaaa", "baa")
    -1
    >>> strStr("test", "")
    0
    """
    if needle == "":
        return 0
    else:
        return haystack.find(needle)

