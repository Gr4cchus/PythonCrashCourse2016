filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass    # silently fail
        # print("Sorry file not found.")
    else:
        print(contents)
