"""
Problem Statement: Print the number of times each integer has occurred in the array.
"""

def count_occurrences(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    
    for num in sorted(counts.keys()):
        print(f"{num} occurs {counts[num]} times")

count_occurrences("1233414512")

#Amit Kumar 202310101150190