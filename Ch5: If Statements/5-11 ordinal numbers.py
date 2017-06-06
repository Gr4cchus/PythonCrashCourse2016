################################################################################################

numbers = []
for x in range(1, 10):
    numbers.append(x)
print(numbers)

# numb = list(range(10))
# print(numb)

for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(str(number) + 'th')
        # print(number, 'th')
