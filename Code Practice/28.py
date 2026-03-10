"""
Problem: Determine the number of valleys traversed (below sea level).
"""

def count_valleys(steps, path):
    valleys = 0
    level = 0
    for step in path:
        if step == 'U':
            level += 1
            if level == 0:
                valleys += 1
        else:
            level -= 1
    return valleys

#Amit Kumar 202310101150190