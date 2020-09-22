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

print reverse(-123)