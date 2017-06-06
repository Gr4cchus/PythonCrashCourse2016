favorite_numbers = {'person1': ['1', '2'],
                    'person2': ['2'],
                    'person3': ['3'],
                    'person4': ['4'],
                    'person5': ['5'],
                    }

for key, value in favorite_numbers.items():
    print(key + '\'s favorite number is: ')
    for values in value:
        print(values)
