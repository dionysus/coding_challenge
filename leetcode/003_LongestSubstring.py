'''
003. Longest Substring Without Repeating Characters
Difficulty: Medium
Url: leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating 
characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.
'''

'''
intuition:
Starting from last, find the longest substring. 
Compare towards the end.
If a string has reached the end of the previous substring,
then it has reached the last index before a duplicate (or end of string), terminating.
Compare and update max, continuing towards the first letter.

RT: O(n^2): needs to iterate across string of length n, n times
Space: no recursion. only need to keep track of a prev tuple.
'''

def lengthOfLongestSubstring(s: str) -> int:
    
    # base cases
    if s == "":
        return 0

    if len(s) == 1:
        return 1

    maxLen = 0

    # going backwards from the last letter
    for i in range(len(s) - 1, -1, -1):
        
        # first iteration
        if i == len(s) - 1:
            prev = (i, i)

        else:
            curr = (i, i)

            # find substr
            for j in range(i + 1, len(s)):
                # found match
                if s[i] == s[j]:
                    break
                # update curr tuple - extend range
                else:
                    curr = (i, j)
                # found end of prev substr
                if j == prev[1]:
                    break
            
            # update current max
            maxLen = max(maxLen, curr[1] - curr[0] + 1)
            # store prev for next iter
            prev = curr

    return maxLen          


if __name__ == '__main__':
    s = ("", 0)
    val = lengthOfLongestSubstring(s[0])
    print("'{}': {} (expected {})".format(s[0], val, s[1]))

    s = (" ", 1)
    val = lengthOfLongestSubstring(s[0])
    print("'{}': {} (expected {})".format(s[0], val, s[1]))

    s = ("abcabcbb", 3)
    val = lengthOfLongestSubstring(s[0])
    print("'{}': {} (expected {})".format(s[0], val, s[1]))

    s = ("bbbbb", 1)
    val = lengthOfLongestSubstring(s[0])
    print("'{}': {} (expected {})".format(s[0], val, s[1]))

    s = ("pwwkew", 3)
    val = lengthOfLongestSubstring(s[0])
    print("'{}': {} (expected {})".format(s[0], val, s[1]))

    s = ("cdd", 2)
    val = lengthOfLongestSubstring(s[0])
    print("'{}': {} (expected {})".format(s[0], val, s[1]))