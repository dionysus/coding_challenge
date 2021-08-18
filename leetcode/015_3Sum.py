"""
15. 3Sum
difficulty: medium
url: https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    triplets = []

    # make dict of count
    num_dict = {}
    for i in range(len(nums)):
        if nums[i] not in num_dict:
            num_dict[nums[i]] = 0
        num_dict[nums[i]] += 1

    i = 0
    while(i < len(nums)):
        target = nums[i]
        num_dict[target] -= 1
        sumPair = twoSum(nums[i + 1:], -target, num_dict)

        for pair in sumPair:
            triplets.append([target] + pair)

        # next iter
        num_dict[target] = 0
        while (i < len(nums) and nums[i] == target):
            i += 1

    return triplets

def twoSum(nums, target, num_dict):
    pairs = []
    for num in num_dict:
        if num_dict[num] <= 0:
            continue

        diff = target - num
        if (diff in num_dict and
            (diff == num and num_dict[num] >= 2 or
            diff > num and num_dict[diff] >= 1)):
            pairs.append([num, diff])

    return pairs

if __name__ == "__main__":
    test = [-1,0,1,2,-1,-4]
    
    print(threeSum(test))
