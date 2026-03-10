"""
Problem Statement: Move all "#" characters to the front of the string.
"""

def move_hash(s):
    hashes = "".join([c for c in s if c == '#'])
    others = "".join([c for c in s if c != '#'])
    return hashes + others

print(move_hash("Move#Hash#to#Front"))

#Amit Kumar 202310101150190