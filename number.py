# match-case to print if the number is positive, negative, or zero.

def number_match(number):
    match number:
        case int() if number > 0: # can use wildcard case _ if number > 0:
            return "positive"
        case int() if  number < 0:
            return "negative"
        case int() if number == 0:
            return "zero"
        case _:
            return "Invalid input"
        
print(number_match(int(input("Enter any number: "))))