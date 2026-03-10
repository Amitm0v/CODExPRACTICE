"""
Problem: Generate all Pythagorean triplets with values smaller than a given limit.
Input: limit = 20
Output: 3 4 5, 8 6 10, 5 12 13, 15 8 17, 12 16 20
"""

def generate_triplets(limit):
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            for c in range(b, limit + 1):
                if a*a + b*b == c*c:
                    print(a, b, c)

generate_triplets(20)

#Amit Kumar 202310101150190