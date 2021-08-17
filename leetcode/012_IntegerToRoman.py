"""
12. Integer to Roman
Difficulty: Medium
url: https://leetcode.com/problems/integer-to-roman/

Given an integer, convert it to a roman numeral.
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        
        def helper(self, roman, num, numX, charX, char5X, char10X):
            if num >= 9 * numX:
                roman += charX + char10X
                num -= 9 * numX

            if num >= 5 * numX:
                roman += char5X
                num -= 5 * numX;

            if num >= 4 * numX:
                roman += charX + char5X
                num -= 4 * numX

            while num >= numX:
                roman += charX
                num -= numX;

            return roman, num
        
        roman = ""
        
        # handle 1000s
        while num >= 1000:
            roman += "M"
            num -= 1000
        
        # handle 100s
        roman, num = helper(self, roman, num, 100, "C", "D", "M")
        # handle 10s
        roman, num = helper(self, roman, num, 10, "X", "L", "C")
        # handle 1s
        roman, num = helper(self, roman, num, 1,  "I", "V", "X")
        
        return roman