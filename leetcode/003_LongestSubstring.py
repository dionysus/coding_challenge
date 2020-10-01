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
def lengthOfLongestSubstring(s: str) -> int:

    if s == "":
        return 0

    if len(s) == 1:
        return 1

    max = 0

    # going backwards from the last letter
    for i in range(len(s) - 1, -1, -1):
        
        # first iteration
        if i == len(s) - 1:
            prev = (i, i)

        else:
            curr = (i, i)
            # find first match
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    break
                else:
                    curr = (i, j)
                if j == prev[1]:
                    break

            if curr[1] - curr[0] + 1 > max:
                max = curr[1] - curr[0] + 1

            prev = curr

    return max          


if __name__ == '__main__':
    s = ("", 0)
    val = lengthOfLongestSubstring(s[0])
    s = (" ", 1)
    val = lengthOfLongestSubstring(s[0])
    s = ("abcabcbb", 3)
    val = lengthOfLongestSubstring(s[0])
    print("{}: {} (expected {})".format(s[0], val, s[1]))
    s = ("bbbbb", 1)
    val = lengthOfLongestSubstring(s[0])
    print("{}: {} (expected {})".format(s[0], val, s[1]))
    s = ("pwwkew", 3)
    val = lengthOfLongestSubstring(s[0])
    print("{}: {} (expected {})".format(s[0], val, s[1]))
    s = ("cdd", 2)
    val = lengthOfLongestSubstring(s[0])
    print("{}: {} (expected {})".format(s[0], val, s[1]))