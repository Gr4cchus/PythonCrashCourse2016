def make_car(manufacturer, model, **user_info_parameters):
    """Create a dictionary for car details"""
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in user_info_parameters.items():
        car[key] = value
    return car
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
