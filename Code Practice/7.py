"""
Problem Statement: Provide the factors of a given number. 
Ignore signs for negative numbers. If zero, output "No Factors".
"""

def find_factors(n):
    n = abs(n)
    if n == 0:
        print("No Factors")
        return
    
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(str(i))
    print(",".join(factors))

find_factors(54)

#Amit Kumar 202310101150190