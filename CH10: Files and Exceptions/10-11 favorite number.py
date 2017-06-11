import json


filename = 'favorite_numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(input("What is your favorite number: "), f_obj)

with open(filename, 'r') as f_obj:
    file_contents = json.load(f_obj)

print("I know your favorite number! its", file_contents + '.')
