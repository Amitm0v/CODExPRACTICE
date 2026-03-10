"""
Problem Statement: Raj wants to know the maximum marks scored by him in each semester.
The mark should be between 0 to 100; if it goes beyond display "You have entered invalid mark."
"""

def get_max_marks():
    num_semesters = int(input("Enter no of semester: "))
    semester_subjects = []
    
    for i in range(num_semesters):
        subs = int(input(f"Enter no of subjects in {i+1} semester: "))
        semester_subjects.append(subs)
        
    for i in range(num_semesters):
        print(f"Marks obtained in semester {i+1}:")
        marks = list(map(int, input().split()))
        
        invalid = False
        for m in marks:
            if m < 0 or m > 100:
                print("You have entered invalid mark.")
                invalid = True
                break
        
        if not invalid:
            print(f"Maximum mark in {i+1} semester: {max(marks)}")

#Amit Kumar 202310101150190