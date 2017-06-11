
active = True

while active:
    print("Press q to quit")
    try:
        input0 = int(input("Enter a number: "))
        input1 = int(input("Enter a number: "))
    except ValueError:
        print("Sorry but it seems you have not entered a number.")
    else:
        print(input0 + input1)

# how do i do something like this:
# if str(input0) == 'q' or str(input1) == 'q':
#             break
