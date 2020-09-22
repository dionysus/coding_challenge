class Solution(object):
    def findNthDigit(n):
        """
        :type n: int
        :rtype: int
        """
        digitsnum = 0
        num = 0
        digits = 1

        while True:

            nextnumber = num + int('9' + (digits-1)*'0') 
            next = digitsnum + int('9' + (digits-1)*'0') * digits

            if next >= n:
                break
            
            if next < n:
                digitsnum = next
                num = nextnumber
                digits += 1


        remainder = n - digitsnum

        divider = (remainder-1) / digits

        number = (divider + 1) + num

        place = (remainder % digits) - 1

        return int(str(number)[place])
    print findNthDigit(7898)
