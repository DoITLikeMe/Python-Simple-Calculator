def calculator():
    print("Simple Calculator")
    print("Select operation:\nOperations: + , - , / , *\nMemory operations: M+ (add) , M- (extract) , MR ( memory recall) , MC ( memory clear)")
    print("Type 'exit' to quit the calculator.")
    memory = 0.0

    while True:
        print("Current Memory:", memory)
        operation = input("Enter operation: ")

        if operation.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        if operation.upper() in ["M+", "M-", "MR", "MC"]:
            if operation.upper() == "MR":
                print("Memory Recall:", memory)
            elif operation.upper() == "MC":
                print("Memory Cleared.")
                memory = 0.0
            elif operation.upper() in ["M+" , "M-"]:
                try:
                    value= float(input("Enter number to add to memory:"))
                    if operation.upper() == "M+":
                        memory += value
                    else:
                        memory -= value
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            continue
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please select a valid operation.")
            continue
        try:
            num1= float(input("Enter first number: "))
            num2= float(input("Enter second number: "))
            if operation == '+':
                result = num1 + num2
                print(f"The result is : {result}")
            elif operation == '-':
                print(f"The  result is: {num1 - num2}")
            elif operation == "*":
                print(f"The result is: {num1 * num2}")
            elif operation == "/":
                if num2== 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
                print(f"The result is {result}")
        except ValueError:
            print("invalid values. Please enter valid numbers")

if __name__ == "__main__":
    calculator()