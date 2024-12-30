my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

num1 = int(input("შეიყვანეთ პირველი მთელი რიცხვი (num1): "))
num2 = int(input("შეიყვანეთ მეორე მთელი რიცხვი (num2): "))

if num1 > num2:
    sliced_list = my_list[num2:num1]
elif num2 > num1:
    sliced_list = my_list[num1:num2]
else:
    sliced_list = []

print(sliced_list)
