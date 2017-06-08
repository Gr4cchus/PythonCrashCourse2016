from user import User


class Admin(User):
    """A special user, subclass"""
    def __init__(self, fname, lname):
        """Initialize attributes of parent
        Then initialize attributes specific to admin
        """
        super().__init__(fname, lname)
        self.privileges = Privileges()


class Privileges():
    """Model Privileges"""
    def __init__(self):
        """Initialize attributes"""
        self.privileges = ['grant', 'deny', 'ban', 'remove', 'rename']

    def show_privileges(self):
        """List the administrator privileges"""
        print("\nList of administrative privileges: ")
        for privilege in self.privileges:
            print('-', privilege)
