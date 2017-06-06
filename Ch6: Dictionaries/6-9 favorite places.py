favorite_places = {'john': ['Iowa'],
                   'alice': ['Illinois'],
                   'barry': ['Texas', 'Alaska'],
                   }

for key, value in favorite_places.items():
    print("\n" + key.title() + "'s favorite places are:")
    for places in value:
        print("\t" + places.title())
