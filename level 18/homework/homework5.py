# 7) Ask the user to enter a number multiple times and check if it's even or odd. Stop after 5 numbers.

num = 18
num2 = int(input('enter num for multiple: '))
if num * num2 % 2 == 0:
    print('its even')
else:
    print('its odd')