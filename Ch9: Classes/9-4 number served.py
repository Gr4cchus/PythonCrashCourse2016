class Restaurant():
    """Modeling a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name  # attribute
        self.cuisine_type = cuisine_type    # attribute
        self.number_served = 0

    def describe_restaurant(self):  # method
        """Print out restaurant details"""
        print("\nThe restaurant name is", self.restaurant_name, "and cuisine type", self.cuisine_type + ".")

    def open_restaurant(self):
        """Print out whether the restaurant is open"""
        print(self.restaurant_name, "is open.")

    def set_number_served(self, number_served):
        """Adjust the number of served people"""
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """Increment the number of customers who have been served."""
        self.number_served += number_served

restaurant = Restaurant("The Outback", "Americanized Australian")   # instance
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)

restaurant.set_number_served(90)
print(restaurant.number_served)
restaurant.increment_number_served(110)
print(restaurant.number_served)


