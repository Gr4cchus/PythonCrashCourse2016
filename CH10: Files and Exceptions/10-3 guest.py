filename = 'guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(input("What is your name: "))
