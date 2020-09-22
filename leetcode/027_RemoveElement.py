from typing import List


def removeElement(nums: List[int], val: int) -> int:
    """
    Given an array nums and a value val, remove all instances of that value
    in-place and return the new length.

    >>> nums = [3,2,2,3]
    >>> val = 3
    >>> removeElement(nums, val)
    2
    >>> nums[0]
    2
    >>> nums[1]
    2
    >>> nums = [0, 1, 2, 3]
    >>> val = 4
    >>> removeElement(nums, val)
    4
    >>> nums
    [0, 1, 2, 3]
    >>> nums = [3, 3, 3, 3]
    >>> val = 3
    >>> removeElement(nums, val)
    0
    """

    if nums == []:
        return 0

    i = 0
    j = len(nums)

    while i < j:
        if nums[i] == val:
            j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    return i
