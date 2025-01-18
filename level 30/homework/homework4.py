def to_lowercase(mixed_case_string):
    return mixed_case_string.lower()

def capitalize_first_letter(strings_list):
    return [s.capitalize() for s in strings_list]

input_string = "Hello, Python World!"
result = to_lowercase(input_string)
print("Lowercase string:", result)

input_list = ["Lello", "Python", "world"]
capitalized_list = capitalize_first_letter(input_list)
print("Capitalized list:", capitalized_list)
