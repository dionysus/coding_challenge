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

    i = 0
    while(i < len(nums)):
        target = nums[i]
        sumPair = twoSum(nums[i + 1:], -target)

        for pair in sumPair:
            triplets.append([target] + pair)

        while (i < len(nums) and nums[i] == target):
            i += 1

    return triplets

def twoSum(nums, target):
    # build a dictionary of value counts
    num_dict = {}
    for i in range(len(nums)):
        if nums[i] not in num_dict:
            num_dict[nums[i]] = 0
        num_dict[nums[i]] += 1
        
    # look for a match
    pairs = []
    for num in num_dict:
        diff = target - num

        if num == diff:
            if num_dict[num] >= 2:
                pairs.append([num, num])
            
        elif diff in num_dict:
            if num < diff:
                pairs.append([num, diff])

    return pairs

if __name__ == "__main__":
    test = [-1,0,1,2,-1,-4]
    
    print(threeSum(test))
