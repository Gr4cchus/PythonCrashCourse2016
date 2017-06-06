# You don’t have to limit the number of tests you
# create to 10. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py Have at least one True and one False result for
# each of the following:

car = 'honda'
if 'honda' != car:
    print('honda isnt present')
else:
    print('honda is present')

if car.lower() == 'honda':
    print('lower function returns true')

number = 10
if number != 9:
    print('\nnumber is not 9')

if number > 10:
    print('\nnumber is greater than 10')
elif number < 10:
    print('number is less than 10')
else:
    print('number is not greater than or less than 10')

if number >= 10:
    print('\nnumber is greater than or equal to 10')
if number <= 10:
    print('number is less than or equal to 10')

if number == 10 and number == 5 * 2:
    print('\nnumber is 10 && equal to 5 * 2')
if number:
    print('True, variable is not empty')

if 'honda' in car:
    print('\nhonda is in car')  # cant iterate if it was a number
cars = ['honda', 'ford', 'bmw']
if 'toyota' not in cars:
    print('toyota was not found in the cars list')
