# საკლასო დავალება:

# შექმენით ფუნქცია სახელად manual_list, რომელსაც ექნება 4 პარამეტრი: start, end, step, user_num.

# თქვენი დავალებაა, რომ ფუნქციამ დააბრუნოს სია, რომელშიც იქნება რიცხვები არჩეული (start, end, step) დიაპაზონის მიხედვით, უბრალოდ ეს რიცხვები მეტი უნდა იყოს user_num.

# ფუნქცია გამოიძახეთ 3-ჯერ, განსხვავებული არგუმენტებით



def manual_list(start, end, step, user_num):
    return [i for i in range(start, end, step) if i > user_num]

print(manual_list(1, 20, 2, 5))
print(manual_list(10, 50, 5, 20))
print(manual_list(-10, 10, 3, -2))


numbers = [x for x in range(1, 101) if (x % 3 == 0 and x % 5 != 0) or (x % 5 == 0 and x % 3 != 0)]
print(numbers)


palindromes = [x for x in range(10, 201) if str(x) == str(x)[::-1]]
print(palindromes)
