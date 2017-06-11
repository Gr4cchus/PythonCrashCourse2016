class Employee:
    """Employee Characteristics"""
    def __init__(self, fname, lname, salary):
        """Initialize first, last name, salary attributes"""
        self.fname = fname  # attribute
        self.lname = lname
        self.salary = salary

    def give_raise(self, amount=5000):   # method
        """Give an employee a raise"""
        self.salary += amount