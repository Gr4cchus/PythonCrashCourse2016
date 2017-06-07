def make_sandwich(*user_info):  # note its just one '*' for lists?
    """"Print sandwich ingredients"""
    print("Making the following sandwich with the following ingredients:")
    for ingredient in user_info:
        print("- ", ingredient)

order1 = ['lettuce', 'tomato']
order2 = ['lettuce', 'tomato', 'bell peppers']
order3 = ['lettuce', 'tomato', 'onion']
make_sandwich(order1)
make_sandwich(order2)
make_sandwich(order3)


