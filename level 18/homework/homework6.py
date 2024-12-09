# 8) Create a while loop that asks the user to enter a password. Keep asking until they enter the correct password "Goa best". Also print the count of incorrect passwords.

correct_passwor = 'goa best'
guess = input('enter correct password: ')
counter = 0

while guess != correct_passwor:
    guess = input('enter correct password: ')
counter += 1

if guess == correct_passwor:
    print('that correct')
    print(f"Your guess count:",{counter})