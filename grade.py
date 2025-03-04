def classify_grade(percentage):
    if 90 <= percentage <= 100:
        return "A (Excellent)"
    elif 80 <= percentage < 90:
        return "B (Good)"
    elif 70 <= percentage < 80:
        return "C (Average)"
    elif 60 <= percentage < 70:
        return "D (Needs Improvement)"
    else:
        return "F (Fail)"


grade_percentage = float(input("Enter your grade percentage (0-100): "))

if 0 <= grade_percentage <= 100:
    print("Your grade is:", classify_grade(grade_percentage))
else:
    print("Invalid input. Please enter a number between 0 and 100.")