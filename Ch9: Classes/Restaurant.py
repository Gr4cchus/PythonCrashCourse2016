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


class IceCreamStand(Restaurant):
    """A subclass of restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize Ice Cream Stand and attributes of parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def show_flavors(self):
        """Display the ice cream flavors"""
        print("\nThe flavors are:")
        for flavor in self.flavors:
            print('-', flavor)
