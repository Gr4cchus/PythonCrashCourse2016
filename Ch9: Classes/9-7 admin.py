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


class Admin(User):
    """A special user, subclass"""
    def __init__(self, fname, lname):
        """Initialize attributes of parent
        Then initialize attributes specific to admin
        """
        super().__init__(fname, lname)
        self.privileges = ['add', 'remove', 'chown', 'grant']

    def show_privileges(self):
        """List the administrator privileges"""
        print("\nList of administrative privileges: ")
        for privilege in self.privileges:
            print('-', privilege)

admin0 = Admin('h', 'dawg')
admin0.describe_user()
admin0.show_privileges()

# user0 = User('john', 'doe')
# user0.describe_user()
# user0.greet_user()
# user1 = User("Alice", 'greyjoy')
# user1.describe_user()
# user1.greet_user()
