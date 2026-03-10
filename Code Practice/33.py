"""
Given a string, find the first character that does not repeat. [cite: 351]
Logic: Use a frequency dictionary to track counts.
"""

def first_non_repeated(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
        
    for char in s:
        if count[char] == 1:
            return char
    return None

#Amit Kumar 202310101150190