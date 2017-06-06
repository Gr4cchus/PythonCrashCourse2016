cities = {
    'cedar rapids': {
        'country': 'US',
        'population': '100',
        'fact': 'four seasons'
    },
    'chicago': {
        'country': 'US',
        'population': '1000',
        'fact': 'central server distribution'
    },
    'new york': {
        'country': 'US',
        'population': '10000',
        'fact': 'one of the first 12 colonies'
    },
}

for key, value in cities.items():
    print('\n', key)
    for key2, value2 in value.items():
        print(key2, value2)
