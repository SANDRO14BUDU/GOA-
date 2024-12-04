# 4) Write a program that checks if a given number is even or odd.

num = int(input('enter ur number and it will say ur number is odd or even: '))
if num % 2 == 0:
    print(f'{num} is even')
else:
    print(f'{num} is odd')