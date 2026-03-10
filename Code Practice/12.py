"""
Problem: Find the second smallest and second largest element in the array.
Print '-1' if they don't exist.
"""

def second_elements(arr):
    unique_elements = sorted(list(set(arr)))
    if len(unique_elements) < 2:
        print("Second Smallest : -1")
        print("Second Largest : -1")
    else:
        print(f"Second Smallest : {unique_elements[1]}")
        print(f"Second Largest : {unique_elements[-2]}")

#Amit Kumar 202310101150190