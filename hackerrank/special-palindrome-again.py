'''
Special String Again
Difficulty: Medium
www.hackerrank.com/challenges/special-palindrome-again/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count = n
    # letters = []
    for mid in range(n):
        # letters.append(s[mid])

        # odd - middle [.., y, y, (x), y, y, ..]
        prev = mid - 1
        next = mid + 1
        letter = mid - 1
        while (prev >= 0 and next < n):
            if s[letter] == s[prev] == s[next]:
                # letters.append(s[prev:next+1])
                count += 1
                prev -= 1
                next += 1
            else:
                break
                
        # even - [.., (x, x+1), ..]
        prev = mid
        next = mid + 1
        while(prev >= 0 and next < n):
            if s[mid] == s[prev] == s[next]:
                # letters.append(s[prev:next+1])
                count += 1
                prev -= 1
                next += 1
            else:
                break
    
    # print(letters)
    return count
        

if __name__ == '__main__':

    n = 7
    s = "abcbaba"

    result = substrCount(n, s)

    print(result)
