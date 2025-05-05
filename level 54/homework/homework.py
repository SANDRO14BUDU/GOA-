def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")

    except ValueError:
        print("Error: Please enter valid numeric input.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Run the function
divide_numbers()
