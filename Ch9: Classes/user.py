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
