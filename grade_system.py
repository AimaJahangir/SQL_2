# Function to calculate grade

def calculate_grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 80:
        return "B"

    elif marks >= 70:
        return "C"

    elif marks >= 60:
        return "D"

    else:
        return "F"


# Main Program
student_marks = 85

grade = calculate_grade(student_marks)

print("Marks:", student_marks)
print("Grade:", grade)