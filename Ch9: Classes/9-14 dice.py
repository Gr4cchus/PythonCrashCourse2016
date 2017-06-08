"""Defines and rolls dice"""    # modules should have doc strings
from random import randint  # module names written in lower case & _


class Die():    # class names camelCaps
    """Model a die"""
    def __init__(self, sides=6):
        """Initialize the die and attributes"""
        self.sides = sides  # instances written in lower case & _

    def roll_die(self):
        """Roll a dice and print 10 times"""
        print("Rolling", self.sides, "times...")
        for roll in range(self.sides):
            random = randint(1, self.sides)
            print(random)

die6 = Die()
die6.roll_die()

die10 = Die(10)
die10.roll_die()

die20 = Die(20)
die20.roll_die()
