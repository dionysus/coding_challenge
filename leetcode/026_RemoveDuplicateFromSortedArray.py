from typing import List


def removeDuplicates(nums: List[int]) -> int:
    """
    Given a sorted array nums, remove the duplicates in-place such that each
    element appear only once and return the new length.

    >>> nums = []
    >>> removeDuplicates(nums)
    0
    >>> nums
    []
    >>> nums = [1]
    >>> removeDuplicates(nums)
    1
    >>> nums
    [1]
    >>> nums = [1, 1, 1, 1]
    >>> removeDuplicates(nums)
    1
    >>> nums[:1]
    [1]
    >>> nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    >>> removeDuplicates(nums)
    4
    >>> nums[:4]
    [1, 2, 3, 4]
    """

    if nums == []:
        return 0
    if len(nums) == 1:
        return 1

    i = 1
    j = 0

    while i < len(nums):
        if nums[i] != nums[j]:
            j += 1
            if i - j > 0:
                nums[i], nums[j] = nums[j], nums[i]
        i += 1
    return j + 1
