'''
167. Two Sum II - Input array is sorted
URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Given an array of integers that is already sorted in ascending order, find two
numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add
up to the target, where index1 must be less than index2.
'''

def two_sum (numbers, target):
  i = 0
  j = len(numbers) - 1
  while i < j:
    if numbers[i] + numbers[j] == target:
      return [i + 1, j + 1]
    elif numbers[i] + numbers[j] < target:
      i += 1
    elif numbers[i] + numbers[j] > target:
      j -= 1

  return None

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(two_sum(nums, target))

    nums = [2,3,4]
    target = 6
    print(two_sum(nums, target))

    nums = [-1, 0]
    target = -1
    print(two_sum(nums, target))