# Grade Point Average
letter_grades = {
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'D-': 0.7,
    'F': 0.0,
}

#Total Grades
grade_input = 5

#List of Grades
grades = []

print("This program calculates grade point average")
for i in range(grade_input):
    grade = input("Please enter course {} letter grade: " .format(i+1))
    grades.append(grade)

try:
    sum = sum([letter_grades[i] for i in grades])
    print("Your GPA for last semester was: ", sum / len(grades))

except KeyError:
    print("You entered a wrong grade.")

