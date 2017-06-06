favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

people = ['jen', 'sarah', 'edward', 'phil', 'john']

for name in favorite_languages.keys():  # praise submission's
    print(" Hi " + name.title() +
          ", thank you for your submission.")

for subjects in people:
    if subjects not in favorite_languages:  # check for people without submissions
        print(subjects.title(), "needs to make a submission.")

