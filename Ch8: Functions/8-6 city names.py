def city_country(city, country):
    """"Display information about a city"""
    print(city.title() + ",", country.title())


while True:
    print("\nEnter city, country:")
    city = input("city: ")
    country = input("country: ")
    city_country(city, country)
