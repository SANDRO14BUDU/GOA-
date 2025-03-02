# საკლასო დავალება:

# შექმენით dictionary, სადაც იქნება შემდეგი გასაღებები: name, surname, academy, fav-color, city, goa-student, age, fav-programming-lang

# dict1 = {
#     "name": "sandro",
#     'surname': 'mchedlidze',
#     'academy': 'GOA',
#     'fav-color': 'green',
#     'city': 'rustavi',
#     'goa-stundet': True,
#     'age': '15',
#     'fav-proggraming-lang': 'css and html'
# }

# print(dict1)


my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "occupation": "Engineer",
    "hobby": "Reading"
}

print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Key-Value Pairs:", my_dict.items())

for key, value in my_dict.items():
    print(f"{key}: {value}")