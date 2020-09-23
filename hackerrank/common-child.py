'''
Common Child
Difficulty: Medium
www.hackerrank.com/challenges/common-child/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
# alpha = ord('A')


def letterCount(s):
    dic = {} # keep track of indiceds with a dict

    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = [i]
        else:
            dic[s[i]].append(i)
    
    return dic

def commonChild(s1, s2):

    dicA = letterCount(s1)
    dicB = letterCount(s2)

    strA = ""
    for letter in s1:
        if dicB.get(letter) is not None:
            strA += letter
    strB = ""
    for letter in s2:
        if dicA.get(letter) is not None:
            strB += letter

    dicA = letterCount(strA)
    dicB = letterCount(strB)

    print("{}: {}".format(strA, dicA))
    print("{}: {}".format(strB, dicB))

    return helper(0, 0, strA, strB, 0, dicA, dicB, "", "")
    
def helper(a, b, strA, strB, length, dicA, dicB, word, seq):

    # if strA == strB:
    #     return length + len(strA)

    if len(strA) == 0 or len(strB) == 0:
        print("{} ({},{}): {} ({})".format(length, a, b, word, seq))
        return length

    else:
        # w/o first letter of A
        woA = helper(a+1, b, strA[1:], strB, length, dicA, dicB, word, seq)
        
        # with first letter of A
        wA = 0
        for indB in dicB[strA[0]]:
            if indB >= b:
                # match found at strB[indB]
                wA = max(wA, helper(a+1, indB+1, strA[1:], strB[indB+1:], length+1, dicA, dicB, word + strA[0], seq + "A{}B{}".format(a, indB)))

        return max(wA, woA)



if __name__ == '__main__':

    s1 = "SHINCHAN"
    s2 = "NOHARAAA"
    s3 = "ABCDEF"
    s4 = "FBDAMN"
    s5 = "HARRY"
    s6 = "SALLY"
    s7 = "AAAA"
    s8 = "AAAA"

    # print("{} and {}: {} (expect {})".format(s1, s2, commonChild(s1,s2), 3))
    # print("{} and {}: {} (expect {})".format(s3, s4, commonChild(s3,s4), 2))
    # print("{} and {}: {} (expect {})".format(s5, s6, commonChild(s5,s6), 2))
    print("{} and {}: {} (expect {})".format(s7, s8, commonChild(s7,s8), "X"))