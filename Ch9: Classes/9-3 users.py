# class Restaurant():
#     """Modeling a restaurant"""
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name  # attribute
#         self.cuisine_type = cuisine_type    # attribute
#
#     def describe_restaurant(self):  # method
#         """Print out restaurant details"""
#         print("\nThe restaurant name is", self.restaurant_name, "and cuisine type", self.cuisine_type + ".")
#
#     def open_restaurant(self):
#         """Print out whether the restaurant is open"""
#         print(self.restaurant_name, "is open.")
#
# restaurant = Restaurant("The Outback", "Americanized Australian")   # instance
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
#
# restaurant1 = Restaurant("Texas Roadhouse", "Steakhouse")
# restaurant1.describe_restaurant()
# restaurant2 = Restaurant("Applebee's", "Grill & Bar")
# restaurant2.describe_restaurant()


class User():
    """Model a user"""
    def __init__(self, fname, lname):
        """Initialize first and last name attributes."""
        self.fname = fname
        self.lname = lname

    def describe_user(self):
        """Print out user details"""
        print("\nUser name is:", self.fname, self.lname)

    def greet_user(self):
        """Print out a greeting to the user."""
        print("Hello", self.fname, self.lname, "it is great to see you!")

user0 = User('john', 'doe')
user0.describe_user()
user0.greet_user()
user1 = User("Alice", 'greyjoy')
user1.describe_user()
user1.greet_user()
