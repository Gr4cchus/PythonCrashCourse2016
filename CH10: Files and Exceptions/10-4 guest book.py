filename = 'guest_book.txt'
active = True

with open(filename, 'w') as file_object:
    print("Press q to quit")
    while active:
        name = input("What is your name: ")
        if name == 'q':
            break
        print("Welcome", name + '.')
        name += '\n'
        file_object.write(name)
