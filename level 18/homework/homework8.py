num1 = int(input('enter first number '))
num2 = int(input('enter second number '))
math = input('(choose) + - / * ')


if math == '+':
    print(num1 + num2) and print(num2 + num1)
elif math == '-':
    print(num1 - num2) and print(num2 - num1)
elif math == '/':
    print(num1 / num2) and print(num2 / num1)
elif math == '*':
    print(num1 * num2) and print(num2 * num1)