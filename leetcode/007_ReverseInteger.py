'''
7. Reverse Integer
Difficulty: Easy
URL: https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within 
the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this 
problem, assume that your function returns 0 when the reversed integer overflows.
'''

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    
    if x < 0:
        neg = True
        x *= -1
    else:
        neg = False
        
    num = str(x)
    newnum=''
    i = 1
    
    while i <= len(num):
        newnum += num[len(num)-i]
        i += 1
        
    final = int(newnum)
    
    if neg:
        final *= -1
        
    if final > 2147483647 or final < -2147483648:
        return 0
    
    return final

if __name__ == "__main__":
    print(reverse(-123))