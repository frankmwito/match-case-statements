# perform operations(add, subtract, multiply, divide) as input and match-case to perform that operation on two numbers

def arithmetic(arithmetics):
    arithmetics = arithmetics.lower()
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    match arithmetics:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 != 0:  # Prevent division by zero
                return num1 / num2
            else:
                return "Cannot divide by zero"
        case _:
            return "Invalid operation"
        
print(arithmetic(input("Enter your preffered operation in words: ")))