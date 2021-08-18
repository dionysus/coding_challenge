"""
039. Combination Sum
difficulty: medium
url: https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers 
sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen 
numbers is different.

It is guaranteed that the number of unique combinations that sum up to target 
is less than 150 combinations for the given input.
"""


def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    candidates.sort()
    return helper(candidates, target)

def helper(candidates, target):

    if target < 0:
        #bad
        return None

    if target == 0:
        # nice
        return []

    res = []

    for i in range(len(candidates)):

        candidate = candidates[i]
        newTarget = target - candidate
        combos = helper(candidates[i:], newTarget)

        if combos == None:
            continue
        
        lst = []
        for combo in combos:
            lst.append([candidate] + combos)
        res.extend(lst)

    return res

if __name__ == "__main__":
    candidates = [2,3,5]
    target = 8
    print(combinationSum(candidates, target))