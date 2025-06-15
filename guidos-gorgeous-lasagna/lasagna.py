"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """preparation_time_in_minutes
    :param number_of_layers: int - number of layers.
    :return: int - total time to make all layers.
    """
    return number_of_layers * 2

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 0

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """preparation_time_in_minutes
    :param number_of_layers: int - number of layers.
    :param elapsed_bake_time: int - time already spent cooking.
    :return: int - total time to make all layers and cook the food.
    """
    return (number_of_layers * 2) + elapsed_bake_time

print(bake_time_remaining(23))
print(preparation_time_in_minutes(4))
print(elapsed_time_in_minutes(5,31))
print(bake_time_remaining.__doc__)
print(preparation_time_in_minutes.__doc__)
print(elapsed_time_in_minutes.__doc__)