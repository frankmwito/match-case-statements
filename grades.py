def message(grade):
    grade = grade.upper()  # Convert the grade to uppercase
    match grade:
        case 'A':
            return "Excellent"
        case 'B':
            return "Good"
        case 'C':
            return "Average"
        case 'D':
            return "Poor"
        case 'F':
            return "Fail"
        case _:
            return "Invalid grade"

# Test the function
print(message(grade='b'))  # Example with lowercase input
