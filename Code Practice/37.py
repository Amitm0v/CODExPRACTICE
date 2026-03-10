"""
Problem: Return true if s can become goal after shifts.
"""

def rotate_check(s, goal):
    return len(s) == len(goal) and goal in (s + s)

#Amit Kumar 202310101150190