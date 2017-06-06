prompt = "What is your age: "
age = ''

while age != "quit":
    age = input(prompt)
    if int(age) < 3:
        print("The ticket is free")
    elif int(age) >= 3 and int(age) <= 12:
        print("The ticket is $10")
    else:
        print("The ticket is $15")
