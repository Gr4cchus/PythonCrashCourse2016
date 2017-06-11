"""A collection of functions for working with cities."""

def city_country(city, country, population=''):
    """Return a string like 'Santiago, Chile'."""
    if population:
        return city.title() + ", " + country.title() + ' - ' + population
    else:
        return city.title() + ", " + country.title()

