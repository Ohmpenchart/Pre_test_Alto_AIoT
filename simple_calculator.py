import math

def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    elif operator == 'sqrt':
        if num1 < 0:
            return "Error: Negative value in sqrt"
        return math.sqrt(num1)
    elif operator == 'pow':
        return num1 ** num2
    else:
        return "Error: Invalid operator"
while 1:
    num1 = input("Enter the first number: ")
    if num1 =="":
        break
    num1=float(num1)
    operator = input("Enter an arithmetic operator (+, -, *, /,sqrt,pow): ")
    if operator == "sqrt" :
        num2=1
    else :
        num2 = float(input("Enter the second number: "))

    result = calculator(num1, num2, operator)
    print("Result:", result)
print("end")
    
    
    