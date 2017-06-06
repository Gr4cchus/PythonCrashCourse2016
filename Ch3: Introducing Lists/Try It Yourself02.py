# If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner Then use your list to print a message to each person, inviting
# them to dinner
names = ['alpha', 'bravo', 'charlie']
print("Join me " + names[0] + " for dinner.")
print("Join me " + names[1] + " for dinner.")
print("Join me " + names.pop(2) + " for dinner.\n")
names.insert(2, "charlie")


# You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations You’ll have to think of
# someone else to invite
print(names.pop(2) + " can not make it.")
names.append("delta")
print("Looks like it will be " + str(names[:]) + " instead.\n")


# You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner
names.insert(0, "charlie")
names.insert(2, "kendrick")
names.append("echo")
print("A bigger tables was found for " + str(names) + ", roll 6 for free drinks.\n")

# You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests
print("Only two permitted")
print(" Sorry", names.pop(), names.pop(), names.pop(), names.pop(),
      "but this table is taken.")
print("Join us", names[:])
del names[:]
print(names)
