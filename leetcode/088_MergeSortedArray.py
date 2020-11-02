'''
88. Merge Sorted Array
URL: https://leetcode.com/problems/merge-sorted-array/

Given two sorted integer arrays nums1 and nums2, 
merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold 
additional elements from nums2.

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''
from typing import List

class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    '''
    two index
    '''
    if n == 0:
      return nums1
    i = 0
    j = 0
    # while nums1 has elements larger than nums2
    while i < m and j < n:
      if nums1[i] > nums2[j]:
        nums1[i+1:] = nums1[i:m]
        nums1[i] = nums2[j]
        j += 1
        m += 1
      i += 1
    # copy rest of nums2
    if j < n:
      nums1[i:] = nums2[j:]


if __name__ == "__main__":

  # nums1 = [1,2,3,0,0,0]
  # m = 3
  # nums2 = [2,5,6]
  # n = 3

  nums1 = [2,0]
  m = 1
  nums2 = [1]
  n = 1

  nums1 = [4,5,6,0,0,0]
  m = 3
  nums2 = [1,2,3]
  n = 3

  test = Solution()
  test.merge(nums1, m, nums2, n)
  print(nums1)