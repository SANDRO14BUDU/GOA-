def prompt_number():
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        print(f"You entered the number: {number}")
    except ValueError:
        print("Error: That is not a valid number.")

prompt_number()
