import unittest

from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    """Tests for city_function.py"""

    def test_city_country(self):
        """Does 'Santiago, Chile' print correctly?"""
        formatted_name = city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

unittest.main()
