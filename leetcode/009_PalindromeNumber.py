def isPalindrome(x):

	num = str(x)
	i = 0

	while i < (len(num)/2):
		if num[i] != num[(len(num)-1)-i]:
			return False
		else: 
			i += 1
	return True

#print isPalindrome(2121212)