"""Test case for '11-3 employee.py'."""
import unittest

from employee import Employee


class EmployeeTestCase(unittest.TestCase):
    """Tests for the module employee.py"""
    def setUp(self):
        """Make an employee"""
        self.john = Employee('john', 'doe', 100000)

    def test_give_default_raise(self):
        """Test for default raise"""
        self.john.give_raise()
        self.assertEqual(self.john.salary, 105000)

    def test_give_custom_raise(self):
        """Test to set custom raise"""
        self.john.give_raise(10000)
        self.assertEqual(self.john.salary, 110000)

unittest.main()
