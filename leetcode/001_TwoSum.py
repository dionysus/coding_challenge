class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # pop off lastnumber in nums, 
        # find pop difference from target
        # difference in nums
        #    if true:
        #        search>> nums.index(difference)
        #   if not:
        #        repeat with next number in list 

        while True:

            search = nums.pop()
            search_index = len(nums)
            difference = target - search

            if difference in nums:
                return [nums.index(difference), search_index]
                break
