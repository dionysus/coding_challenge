'''
283. Move Zeroes
URL: https://leetcode.com/problems/move-zeroes/
Difficulty: Easy

Given an array nums, write a function to move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.
'''

def moveZeroes(nums: List[int]) -> None:
	"""
	Do not return anything, modify nums in-place instead.
	"""        
	j = 1 # tracking non-zeros
	
	for i in range(len(nums)):
		if j >= len(nums):
			break
		
		# swap 0 with next 
		if nums[i] == 0:
			# find next non-zero    
			while j < len(nums) - 1 and nums[j] == 0:
				j += 1
			# swap
			nums[j], nums[i] = nums[i], nums[j]
			
		# next
		j += 1