class User():
    """Model a user"""
    def __init__(self, fname, lname):
        """Initialize first and last name attributes."""
        self.fname = fname
        self.lname = lname
        self.login_attempts = 0

    def describe_user(self):
        """Print out user details"""
        print("\nUser name is:", self.fname, self.lname)

    def greet_user(self):
        """Print out a greeting to the user."""
        print("Hello", self.fname, self.lname, "it is great to see you!")

    def increment_login_attempts(self):
        """Increment login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to zero"""
        self.login_attempts = 0

user0 = User('john', 'doe')
user0.describe_user()
user0.greet_user()
user1 = User("Alice", 'greyjoy')
user1.describe_user()
user1.greet_user()

user3 = User('john', 'wick')
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()
print(user3.login_attempts)
user3.reset_login_attempts()
print(user3.login_attempts)
