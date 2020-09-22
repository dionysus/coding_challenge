def singleNumber(nums):
	"""
	>>> singleNumber([2, 1, 2])
	1
	"""
	nums.sort()
	i = 0
	while i < len(nums):
		if i == len(nums) - 1:
			return nums[i]
		if nums[i] == nums[i + 1]:
			i += 2
		else:
			return nums[i]

if __name__ == "__main__":
	import doctest
	doctest.testmod()
	print("*" * 20)
	print("doctests: done")
	print("*" * 20)
