"""
You are given an array. The task is to reverse the array and print it.
Logic: Swap elements from start and end moving towards the middle.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

print(reverse_array([5, 4, 3, 2, 1]))

#Amit Kumar 202310101150190