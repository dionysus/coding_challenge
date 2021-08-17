"""
5. Longest Palindromic Substring
difficulty: Medium
url: https://leetcode.com/problems/longest-palindromic-substring/

Given a string `s`, return the longest palindromic substring in `s`.
"""

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    def getLongestOddString(center, s):
        left = center
        right = center
        while (left - 1 >= 0 and right + 1 <= len(s) - 1):
            if (s[left - 1] == s[right + 1]):
                left -= 1
                right += 1
            else:
                break

        return s[left : right + 1]

    def getLongestEvenString(center, s):
        left = center
        right = center + 1

        if (left == len(s) - 1 or s[left] != s[right]):
            return ""
        
        while (left - 1 >= 0 and right + 1 <= len(s) - 1):
            if (s[left - 1] == s[right + 1]):
                left -= 1
                right += 1
            else:
                break

        return s[left : right + 1]

    if (len (s) == 1):
        return s

    longestSub = s[0]

    for center in range(len(s)):
        oddSub = getLongestOddString(center, s)
        evenSub = getLongestEvenString(center, s)
        if len(oddSub) > len(longestSub):
            longestSub = oddSub
        if len(evenSub) > len(longestSub):
            longestSub = evenSub

    return longestSub

if __name__ == "__main__":

    test = "esbtzjaaijqkgmtaajpsdfiqtvxsgfvijpxrvxgfumsuprzlyvhclgkhccmcnquukivlpnjlfteljvykbddtrpmxzcrdqinsnlsteonhcegtkoszzonkwjevlasgjlcquzuhdmmkhfniozhuphcfkeobturbuoefhmtgcvhlsezvkpgfebbdbhiuwdcftenihseorykdguoqotqyscwymtjejpdzqepjkadtftzwebxwyuqwyeegwxhroaaymusddwnjkvsvrwwsmolmidoybsotaqufhepinkkxicvzrgbgsarmizugbvtzfxghkhthzpuetufqvigmyhmlsgfaaqmmlblxbqxpluhaawqkdluwfirfngbhdkjjyfsxglsnakskcbsyafqpwmwmoxjwlhjduayqyzmpkmrjhbqyhongfdxmuwaqgjkcpatgbrqdllbzodnrifvhcfvgbixbwywanivsdjnbrgskyifgvksadvgzzzuogzcukskjxbohofdimkmyqypyuexypwnjlrfpbtkqyngvxjcwvngmilgwbpcsseoywetatfjijsbcekaixvqreelnlmdonknmxerjjhvmqiztsgjkijjtcyetuygqgsikxctvpxrqtuhxreidhwcklkkjayvqdzqqapgdqaapefzjfngdvjsiiivnkfimqkkucltgavwlakcfyhnpgmqxgfyjziliyqhugphhjtlllgtlcsibfdktzhcfuallqlonbsgyyvvyarvaxmchtyrtkgekkmhejwvsuumhcfcyncgeqtltfmhtlsfswaqpmwpjwgvksvazhwyrzwhyjjdbphhjcmurdcgtbvpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquhiafjqaionbrjbjksxaezosxqmncejjptcksnoq"
    # test = "cbbd"
    # test = "bb"
    # test = "babad"
    print(longestPalindrome(test))
