
try:
    input0 = int(input("Enter a number: "))
    input1 = int(input("Enter a number: "))
except ValueError:
    print("Sorry but it seems you have not entered a number.")
else:
    print(input0 + input1)
