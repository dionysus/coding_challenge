def lengthOfLastWord(s):
	
#sum = 0
		
	#if len(s) < 1
	#   return sum
	
	##1. Remove end _'s
	#if s[-1] == ' '
	#   loop: remove end _'s
	
	##2. Count length of remaining
	#if s[] not empty
	#   loop: count letters
	#   if last != ' ', add += sum
	
	
	if len(s) < 1:
		return 0	# if s == ''
	while s[-1] == ' ':
		s = s[:-1]
		if len(s) < 1:
			return 0	
	sum = 0
	while len(s) > 0:
		if s[-1] == ' ':
			break
		else:
			s = s[:-1]
			sum += 1
	return sum

print lengthOfLastWord('   ')