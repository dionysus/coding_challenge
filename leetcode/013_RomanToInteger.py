def romanToInt(s):

	symbols = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	combo = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C':['D', 'M']}

	sum = 0
	index = 0

	while index < len(s):
		if index + 1 < len(s) and s[index] in combo and s[index + 1] in combo[s[index]]:
			sum -= symbols[s[index]]
			index += 1
		sum += symbols[s[index]]
		index += 1
	return sum

print romanToInt("MCMLIX")
