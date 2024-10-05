def grading_system(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


score = float(input("Enter your score: "))


print(f"Your grade is: {grading_system(score)}")