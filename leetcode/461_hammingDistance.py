'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''

def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    
    >>> hammingDistance(1, 4)
    2
    
    """
    
    bins = [int(str(bin(x))[2:]), int(str(bin(y))[2:])]
    bins.sort()
    bins = [str(bins[0]), str(bins[1])]

    ham = 0
    
    for i in range(1, len(bins[1]) + 1):
        a = '0'
        if i <= len(bins[0]):
            a = bins[0][-i]
        if a != bins[1][-i]:
            ham += 1
        #print ('[', a, ':', bins[1][-i], ']', ':', ham)
    return ham