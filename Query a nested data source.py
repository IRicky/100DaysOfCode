"""Given the provided cars dictionary:

Get all Jeeps
Get the first car of every manufacturer.
Get all vehicles containing the string Trail in their names (should work for other grep too)
Sort the models (values) alphabetically
See the docstrings and tests for more details. Have fun!

Update 18th of Sept 2018: as concluded in the forum it is better to pass the cars dict into each function to make its scope local."""

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}
from operator import itemgetter
from collections import OrderedDict


def get_all_jeeps(cars=cars):
    for key, value in cars.items():
        output = str.join(", ", value)
    return output


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return list(value[0] for key, value in cars.items())


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    output = sorted(value[value.index(v)] for key, value in cars.items() for v in value if grep.lower() in v.lower())
    return output


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    output={}
    for key,value in cars.items():
        output[key]=sorted(list(value))
    return (output)

print(get_all_jeeps())
print(get_first_model_each_manufacturer())
print(get_all_matching_models())
print(sort_car_models())
