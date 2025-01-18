# name = input("Enter your name: ")

# choice = input("Enter your choice ('u' for uppercase, 'l' for lowercase): ")

# if choice == "u":
#     print("Your name in uppercase:", name.upper())
# elif choice == "l":
#     print("Your name in lowercase:", name.lower())
# else:
#     print("Wrong information.")


# შექმენით ფუნქცია, სახელად manual_find, რომელსაც გაწერილი ექნება 2 პარამეტრი: main_string და str_to_find.
# ამ ფუნქციის დავალებაა რომ main_string-ში იპოვოს str_to_find მერამდენე ინდექსზეა.
# თუ მთავარ სთრინგში საძიებელი სთრინგი უბრალოდ არ გვაქვს, დავბეჭდოთ -1

def manual_find(main_string, str_to_find):
    main_length = 0
    for _ in main_string:
        main_length += 1

    find_length = 0
    for _ in str_to_find:
        find_length += 1

    for i in range(main_length - find_length + 1):
        match = True
        for j in range(find_length):
            if main_string[i + j] != str_to_find[j]:
                match = False
                break
        if match:
            return i
    return -1

main_string = input("Enter the main string: ")
str_to_find = input("Enter the string to find: ")

result = manual_find(main_string, str_to_find)
print(result)


