import math

while True:
    num1 = float(input("Enter your first number : "))  #define first number
    num2 = float(input("Enter your second number : "))  #define second number
    operator = input("Enter the operator(+, -, *, /, **, %, //): ") # define the operator which function you want to perform
    
    if operator == "sqrt":
        square_root = math.sqrt(num1)
        print(f"The square root of {num1} is = {square_root}")

    try:
        if operator == "+":
            result = num1 + num2 # evaluate sum result
        elif operator == "-":
            result = num1 - num2 # evaluate subtraction result
        elif operator == "*":
            result = num1 * num2 # evaluate multiplication result           
        elif operator == "/":
            result = num1 / num2 # evaluate division result
        elif operator == "**":
            result = num1 ** num2 # evaluate exponentiation result
        elif operator == "%":
            result = num1 % num2 # evaluate modulus result
        elif operator == "//":
            result = num1 // num2 # evaluate floor division result  
        else:
            result = "Invalid operator" # if invalid character entered 
    except ZeroDivisionError:       # handles the divide by zero error
        result = "Division by zero error"
    

    print(f"The result of {num1} {operator} {num2} is = {result}") # it specfically prints the result in proper understandable way

    

    again = input("Do you want to calculate again? (yes/no)").lower()  # asks the user if they want to repeat the calculation
    if again != "yes":   # if no then breaks out of the loop 
        break




