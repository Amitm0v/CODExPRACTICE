"""
Problem: Find the longest common prefix string amongst an array of strings.
"""

def longest_common_prefix(strs):
    if not strs: return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
    return prefix

#Amit Kumar 202310101150190