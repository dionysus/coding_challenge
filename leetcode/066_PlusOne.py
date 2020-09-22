#Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

#You may assume the integer do not contain any leading zero, except the number 0 itself.

#The digits are stored such that the most significant digit is at the head of the list.

def plusOne(digits):
	"""
	:type digits: List[int]
	:rtype: List[int]
	"""
	if len(digits) < 1:
		return None
	last = digits.pop()

	if last != 9:
		last += 1
		return digits + [last]
	else:
		last = 0
		if len(digits) == 0:
			return [1] + [last]
		return plusOne(digits) + [last]

#print plusOne([1,1,1,1,1,1,1,1,1,1,1,])
