prompt = "What is your age: "
age = ''
active = True

while active:
    age = input(prompt)
    if age == "quit":
        active = False
        break
        print("bye")    # because break is before this line, it will not print
    elif int(age) < 3:
        print("The ticket is free")
    elif int(age) >= 3 and int(age) <= 12:
        print("The ticket is $10")
    elif int(age) > 12:
        print("The ticket is $15")

