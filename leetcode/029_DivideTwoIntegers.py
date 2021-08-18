
def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """

    if (dividend < 0 and divisor < 0) or (dividend >= 0 and divisor >= 0) :
        divMod = myMod(abs(dividend), abs(divisor), True)
    else: 
        divMod = myMod(abs(dividend), abs(divisor), False)

    if divMod > 2**31 - 1 or divMod < -2**31:
        return 2**31 - 1
    else:
        return divMod

def myMod(dividend, divisor, pos):
    if divisor == 1:
        i = dividend
    else: 
        i = 0
        while dividend >= divisor:
            dividend -= divisor
            i += 1

    if pos:
        return i
    else:
        return -i

if __name__ == "__main__":
    dividend = 1
    divisor = -1
    
    print(divide(dividend, divisor))