def longestPalindrome(s):
    if (s==s[::-1]):
        return s
    else:
        return max([longestPalindrome(s[1:]),longestPalindrome(s[:-1])],key=len)

s="hibabab"

print(longestPalindrome(s))
