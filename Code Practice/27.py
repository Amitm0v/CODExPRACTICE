"""
Problem Statement: Display season name based on month number (1-12).
"""

def get_season():
    month = int(input("Enter month: "))
    if month < 1 or month > 12:
        print("Invalid Month Entered")
    elif 3 <= month <= 5:
        print("Season: Spring")
    elif 6 <= month <= 8:
        print("Season: Summer")
    elif 9 <= month <= 11:
        print("Season: Autumn")
    else:
        print("Season: Winter")

#Amit Kumar 202310101150190