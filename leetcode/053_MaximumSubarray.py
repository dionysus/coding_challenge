from typing import List


def maxSubArray(nums: List[int]) -> int:
    """Given an integer array nums, find the contiguous subarray (containing at
    least one number) which has the largest sum and return its sum.

    >>> maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    8
    """

    return len(nums)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("*" * 20)
    print("doctests: done")
    print("*" * 20)