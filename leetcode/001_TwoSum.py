class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # build a dictionary of value counts
        num_dict = {}
        for i in range(len(nums)):
            if nums[i] not in num_dict:
                num_dict[nums[i]] = []
            num_dict[nums[i]].append(i)
            
        # look for a match
        for num in num_dict:
            diff = target - num

            if num == diff:
                if len(num_dict[num]) == 2:
                    return num_dict[num]

            elif diff in num_dict:
                return num_dict[num] + num_dict[diff][0]