def climbStairs(n):
	"""
	:type n: int
	:rtype: int
	"""
	#fibonnaci sequence starting at 1, 2...

	#fib(n) = fib(n-1) + fib(n-2)

	sequence = [1,2]

	for i in range (0, n-2):

		steps = sequence[i] + sequence[i+1]
		sequence.append(steps)

	return sequence[n-1]

print climbStairs(2)
