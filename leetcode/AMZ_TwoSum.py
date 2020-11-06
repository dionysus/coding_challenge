'''
Two Sum (Amazon variant)
URL: https://leetcode.com/discuss/interview-question/372434

Given an int array nums and an int target, find how many unique pairs in the a
rray such that their sum is equal to target. Return the number of pairs.

Example 1:
Input: nums = [1, 1, 2, 45, 46, 46], target = 47
Output: 2
Explanation:
1 + 46 = 47
2 + 45 = 47

Example 2:
Input: nums = [1, 1], target = 2
Output: 1
Explanation:
1 + 1 = 2
Example 3:

Input: nums = [1, 5, 1, 5], target = 6
Output: 1
Explanation:
[1, 5] and [5, 1] are considered the same.
'''

def two_sum (nums, target):
  # build set (reduce problem size) - O(n)
  # 
  nums.sort()
  count = 0
  if nums.count(target / 2):
    count += 1

  nums = list(set(nums))

  i = 0
  j = len(nums) - 1

  while i < j:
    if nums[i] + nums[j] == target:
      count += 1
      i += 1
      j -= 1
    elif nums[i] + nums[j] < target:
      i += 1
    elif nums[i] + nums[j] > target:
      j -= 1

  return count

if __name__ == "__main__":
    nums = [1, 1, 2, 45, 46, 46]
    target = 47
    print(two_sum(nums, target))

    nums = [1, 1]
    target = 2
    print(two_sum(nums, target))

    nums = [1, 5, 1, 5]
    target = 6
    print(two_sum(nums, target))