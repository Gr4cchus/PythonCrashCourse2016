import unittest

from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """Does 'Santiago, Chile' print correctly?"""
        formatted_name = city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        """Does 'Santiago, Chile - Population_here print correctly"""
        formatted_with_population = city_country('santiago', 'chile', '100')
        self.assertEqual(formatted_with_population, 'Santiago, Chile - 100')

unittest.main()
# final = city_country('santiago', 'chile')
# final = city_country('santiago', 'chile', '100')
# print(final)