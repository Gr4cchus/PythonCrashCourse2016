# Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time
names = ['alpha', 'bravo', 'charlie']
print(names[0])
print(names[1:2])
print(names[-1])


# Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each
# message should be the same, but each message should be personalized with the person’s name
print("Hello " + names[0] + " it is good to see you.")
print("Hello " + names[1] + " it is good to see you.")
print("Hello " + names[2] + " it is good to see you.")


# Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle."
motorcycles = ['Honda', 'Kawasaki']
print("It would be great to have a " + motorcycles[0] + "\nOr " +
      motorcycles[-1] + " motorcycle wouldn't it!")
