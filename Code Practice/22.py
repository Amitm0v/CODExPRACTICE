"""
Problem: Find the number of pairs of integers whose sum is equal to target.
"""

def count_pairs(arr, target):
    count = 0
    freq = {}
    for x in arr:
        complement = target - x
        if complement in freq:
            count += freq[complement]
        freq[x] = freq.get(x, 0) + 1
    return count

#Amit Kumar 202310101150190