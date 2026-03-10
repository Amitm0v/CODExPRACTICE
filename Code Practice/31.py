"""
Given two strings s and t, return true if t is an anagram of s. [cite: 328]
Logic: Count character frequencies in a dictionary and compare.
"""

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
        
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
        
    return True

#Amit Kumar 202310101150190