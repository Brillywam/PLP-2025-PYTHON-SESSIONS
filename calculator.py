def main():
    print("Welcome to the calculator!")
    # ask the user to input the 2 numbers

    print("Please enter the first number:")
    num1 = float(input("Enter the first number: "))

    print("Please enter the second number:")
    num2 = float(input("Enter the second number: "))
    # ask the user to input the operation
    print("Please enter the operation:")
    operation = input("Enter the operation (+, -): ")
    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == "-":
        result(num1 - num2)
        print(f"{num1} - {num2} = {result}")
    else:
        print("Error: Operation not supported. Please enter + or -")
if __name__ == "__main__":   
    main()