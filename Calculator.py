# CALCULATOR
# TASK 2
# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result.
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if x != y:
        return x /y
    else:
        return "Error: Division by zero"

def Calculator():
    print("\nSimple Calculator")
    print("1. Addition")
    print("1. Subtraction")
    print("1. Multiply")
    print("1. Division")
    
    try:
        choice = int(input("Enter choice (1/2/3/4): "))
    except ValueError:
        print("Invalid input, please enter a new number.")
        return
    
    if choice not in [1, 2, 3, 4]:
        print("Invalid choice. please enter a valid number")
        return
    
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

    except ValueError:
        print("Enter the valid number")
        return

    if choice == 1:
        result =  add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == 2:
        result =  subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == 3:
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}") 
    elif choice == 4:
        result = divide(num1, num2)       
        print(f"{num1} / {num2} = {result}")

Calculator()