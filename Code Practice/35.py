"""
Problem: Return the longest palindromic substring in s.
"""

def longest_palindrome(s):
    res = ""
    for i in range(len(s)):
        # odd
        tmp = helper(s, i, i)
        if len(tmp) > len(res): res = tmp
        # even
        tmp = helper(s, i, i + 1)
        if len(tmp) > len(res): res = tmp
    return res

def helper(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]

#Amit Kumar 202310101150190