filename = 'programming_reasons.txt'
active = True

with open(filename, 'a') as file_object:
    print("Press q to quit")
    while active:
        reason = input("Why do you like programming: ")
        if reason == 'q':
            break
        # print("Welcome", name + '.')
        reason += '\n'
        file_object.write(reason)
