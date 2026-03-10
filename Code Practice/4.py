"""
Problem Statement: Write a function to solve the following equation 
a^3 + a^2b + 2a^2b + 2ab^2 + ab^2 + b^3.
Accept three values in order of a, b and c.
"""

def solve_equation(a, b, c):
    result = a**3 + (a**2 * b) + (2 * a**2 * b) + (2 * a * b**2) + (a * b**2) + b**3
    return result

a = int(input())
b = int(input())
c = int(input())
print(solve_equation(a, b, c))

#Amit Kumar 202310101150190