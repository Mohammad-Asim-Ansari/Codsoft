def calculator():
    print("Welcome to the simple calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    choice = input("Enter the operation (+, -, *, /): ")
    if choice == '+':
        result = num1 + num2
        operation = '+'
    elif choice == '-':
        result = num1 - num2
        operation = '-'
    elif choice == '*':
        result = num1 * num2
        operation = '*'
    elif choice == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        operation = '/'
    else:
        print("Invalid operation choice.")
        return
    print(f"{num1} {operation} {num2} = {result}")
calculator()
