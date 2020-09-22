'''
Given a string, find the length of the longest substring without repeating 
characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.
'''

'''
intuition

word = "abcabcbb"
abca
bcab
cabc
abc
bc
cb
b

find indexes of pairs?

a: (0, 3)
b: (1, 4),(4, 6),(6, 7)
c: (2, 5)

Sort by longest
a: (0, 3) = 3
b: (1, 4) = 3
c: (2, 5) = 3
b: (4, 6) = 2
b: (6, 7) = 1

see if intersects with another?
a: (0, 3) = 3
no intersects!

create a tree?

min()

'''