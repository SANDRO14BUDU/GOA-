start = int(input("Enter the starting integer: "))
end = int(input("Enter the ending integer: "))

total = 0
for number in range(start, end + 1):
    total += number

print(f"The sum of numbers between {start} and {end} is: {total}")
