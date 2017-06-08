# class Dog():
#     """A simple attempt to model a dog."""
#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(self.name.title() + " is now sitting.")
#
#     def roll_over(self):
#         """Simulate rolling over in response to a command."""
#         print(self.name.title() + " rolled over!")


class Restaurant():
    """Modeling a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name  # attribute
        self.cuisine_type = cuisine_type    # attribute

    def describe_restaurant(self):  # method
        """Print out restaurant details"""
        print("\nThe restaurant name is", self.restaurant_name, "and cuisine type", self.cuisine_type + ".")

    def open_restaurant(self):
        """Print out whether the restaurant is open"""
        print(self.restaurant_name, "is open.")

restaurant = Restaurant("The Outback", "Americanized Australian")   # instance
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
