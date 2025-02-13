# საკლასო დავალება:

# შექმენით tuple სადაც შეინახება 10 ელემენტი.

# დაბეჭდეთ თითოუელი ელემენტი, ინდექსების გამოყენებით


# okay = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# print(okay[0])
# print(okay[1])
# print(okay[2])
# print(okay[3])
# print(okay[4])
# print(okay[5])
# print(okay[6])
# print(okay[7])
# print(okay[8])
# print(okay[9])



# საკლასო დავალება:

# შექმენით ფუნქცია სახელად no_duplicates, რომელსაც გადაეცემა ერთი პარამეტრი - user_list.

# user_list-ის მონაცემთა ტიპია სია, ხოლო თქვენი დავალებაა რომ ფუნქციამ დააბრუნოს ეს სია იმ სახით, რომ მასში დუპლიკატები არ გვქონდეს. 

# ფუნქცია გამოიძახეთ 3-ჯერ, განსხვავებული არგუმენტებით

def no_duplicates(user_list):
    return list(set(user_list))

list1 = [1, 2, 2, 3, 4, 4, 5]
list2 = ["apple", "banana", "apple", "orange"]
list3 = [7, 8, 9, 7, 8, 10, 11]

print("Unique elements in list1:", no_duplicates(list1))
print("Unique elements in list2:", no_duplicates(list2))
print("Unique elements in list3:", no_duplicates(list3))
