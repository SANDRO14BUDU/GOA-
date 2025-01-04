# შექმენით ფუნქცია სახელად greet, რომელსაც ექნება 1 პარამეტრი. ფუნქციის გამოძახებისას არგუმენტად გადაეცით თქვენი სახელი და ფუნქციამ ასეთი რამ უნდა დაგიბეჭდოთ: "გამარჯობა, {აქ თქვენი სახელი}"

def greet(name):
    print(f"გამარჯობა, {name}")

greet("sandro mchedlidze")


def manual_range(start, end, step):
    for num in range(start, end, step):
        if num % 2 == 0:
            print(num)

manual_range(1, 10, 1)
manual_range(2, 20, 2)
manual_range(5, 25, 3)
manual_range(10, 50, 5)
manual_range(0, 100, 10)


def manual_len(my_list):
    count = 0
    for item in my_list:
        count += 1
    print(count)

manual_len([1, 2, 3, 4, 5])
manual_len(['a', 'b', 'c', 'd'])
manual_len([10, 20, 30])
manual_len([True, False, True])
manual_len([1, 2, 3, 4, 5, 6, 7])
