# try:
#     my_int = 10
#     result = my_int + "text"
# except TypeError:
#     print("TypeError: ვერ მოხერხდა ინტეჯერის და სტრიქონის შეკრება.")

try:
    user_input = input("შეიყვანეთ სახელი ან გვარი: ")
    print(f"მომხმარებლის მიერ შეყვანილი მონაცემი: {user_input}")
except Exception as e:
    print(f"შეცდომა მოხდა: {type(e).__name__} - {e}")
