from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    """
    >>> searchInsert02([], 0)
    0
    >>> searchInsert02([1], 0)
    0
    >>> searchInsert02([0], 1)
    1
    >>> searchInsert([1,3,5,6], 5)
    2
    >>> searchInsert([1,3,5,6], 2)
    1
    >>> searchInsert([1,3,5,6], 7)
    4
    >>> searchInsert([1,3,5,6], 0)
    0
    """
    if nums == []:
        return 0

    for i in range(len(nums)):
        if target <= nums[i]:
            return i

    return len(nums)


def searchInsert02(nums: List[int], target: int) -> int:
    """
    >>> searchInsert02([], 0)
    0
    >>> searchInsert02([1], 0)
    0
    >>> searchInsert02([0], 1)
    1
    >>> searchInsert02([1,3,5,6], 5)
    2
    >>> searchInsert02([1,3,5,6], 2)
    1
    >>> searchInsert02([1,3,5,6], 7)
    4
    >>> searchInsert02([1,3,5,6], 0)
    0
    >>> searchInsert02([1,3,5], 5)
    2
    >>> searchInsert02([1,3,5], 2)
    1
    >>> searchInsert02([1,3,5], 7)
    3
    >>> searchInsert02([1,3,5], 0)
    0
    """
    if nums == []:
        return 0

    if len(nums) == 1:
        if nums[0] < target:
            return 1
        return 0

    mid = len(nums) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return mid + searchInsert02(nums[mid:], target)
    else:
        return searchInsert02(nums[:mid], target)
