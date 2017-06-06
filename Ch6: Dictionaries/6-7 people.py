person0 = {'first name': 'john',
           'last name': 'doe',
           'age': '20',
           'city': 'Cedar Rapids'}

person1 = {'first name': 'mary',
           'last name': 'doe',
           'age': '20',
           'city': 'Cedar Rapids'}

person2 = {'first name': 'ben',
           'last name': 'doe',
           'age': '20',
           'city': 'Cedar Rapids'}

people = [person0, person1, person2]

for person in people:
    for key, value in person.items():
        print(key, value)
