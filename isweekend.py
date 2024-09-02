def is_weekend(day):
    day = day.lower()  # Convert the input to lowercase
    match day:
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "It's a weekday"
        case "saturday" | "sunday":
            return "It's a weekend"
        case _:
            return "Invalid day"

# Prompt the user for input
user_input = input("Enter a day of the week: ")
print(is_weekend(user_input))
