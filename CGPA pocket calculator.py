# PERSONAL POCKET CGPA CALCULATOR

print("PERSONAL POCKET CGPA CALCULATOR")

n = int(input("Enter the number of courses: "))

total_grade_points = 0
total_units = 0

for i in range(1, n + 1):
    print("\nCourse", i)

    unit = int(input("Enter course unit: "))
    score = int(input("Enter score: "))

    # Determine grade point using selection statements
    if score >= 70:
        grade = "A"
        gp = 5
    elif score >= 60:
        grade = "B"
        gp = 4
    elif score >= 50:
        grade = "C"
        gp = 3
    elif score >= 45:
        grade = "D"
        gp = 2
    elif score >= 40:
        grade = "E"
        gp = 1
    else:
        grade = "F"
        gp = 0

    print("Grade:", grade)
    print("Grade Point:", gp)

    total_grade_points += gp * unit
    total_units += unit

cgpa = total_grade_points / total_units

print("\n========== RESULT ==========")
print("Total Course Units:", total_units)
print("Total Grade Points:", total_grade_points)
print("CGPA =", round(cgpa, 2))

# Class of Degree
if cgpa >= 4.50:
    print("Class of Degree: First Class")
elif cgpa >= 3.50:
    print("Class of Degree: Second Class Upper")
elif cgpa >= 2.40:
    print("Class of Degree: Second Class Lower")
elif cgpa >= 1.50:
    print("Class of Degree: Third Class")
else:
    print("Class of Degree: Pass")