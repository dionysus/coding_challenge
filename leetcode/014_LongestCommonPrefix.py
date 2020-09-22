'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Input: ["flower","flow","flight"]
Output: "fl"

'''

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    
    >>> longestCommonPrefix(["flower","flow","flight"])
    'fl'
    
    """
    
    if len(strs) == 0:
        return ''
    
    if len(strs) == 1:
        return strs[0]
    
    common = ''
    comp = ''
    i = 1
    
    while True:
        j = 0
        
        #for each word, test letter to comp
        for word in strs:
            if j == 0: 
                comp = strs[j][: i]
            elif i > len(strs[j]) or strs[j][: i] != comp:
                return common
            j += 1
        
        common = comp
        i += 1

    
    

