"""
Problem Statement: Find the item that has the minimum discount amount to avoid buying it.
Input: item name, price, discount percentage.
"""

def find_min_discount():
    n = int(input())
    items = []
    for _ in range(n):
        line = input().split(',')
        name = line[0].strip()
        price = int(line[1].strip())
        disc_percent = int(line[2].strip())
        disc_amount = (price * disc_percent) // 100
        items.append((name, disc_amount))
    
    min_val = min(items, key=lambda x: x[1])[1]
    for name, amt in items:
        if amt == min_val:
            print(name)

#Amit Kumar 202310101150190