"""
Problem: Implement binary search to find target index in sorted array.
Input: [1, 2, 3, 4, 5, 6, 7, 8, 9], Target: 4
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

#Amit Kumar 202310101150190