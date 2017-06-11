import json

filename = 'favorite_numbers.json'

try:
    with open(filename, 'r') as f_obj:
        file_contents = json.load(f_obj)
except FileNotFoundError:
    print("File not found")
    with open(filename, 'w') as f_obj:
        json.dump(input("What is your favorite number: "), f_obj)
    print("Remembering your number.")
else:
    print("I know your favorite number! its", file_contents + '.')
