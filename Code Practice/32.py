"""
Given a string s, find the first non-repeating character in it and return its index. [cite: 337]
Logic: One pass to build a frequency map, second pass to find the first index with count 1.
"""

def first_uniq_char(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
        
    for i in range(len(s)):
        if count[s[i]] == 1:
            return i
    return -1

#Amit Kumar 202310101150190