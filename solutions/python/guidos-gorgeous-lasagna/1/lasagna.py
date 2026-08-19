"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes.

    Parameters:
        number_of_layers (int): The number of layers.

    Returns:
        int: The time (in minutes) it takes to prepare. Derived from 'PREPARATION_TIME'.

    Function that takes the number_of_layers you want to add
    to the lasagna as an argument and returns how many minutes you would
    spend making them. Each layer takes 'PREPARATION_TIME' to prepare.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Parameters:
        number_of_layers (int): The number of layers.
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The time (in minutes) spent in the kitchen.

    Function that returns the total minutes spent in the kitchen cooking
    — preparation time layering + the time the lasagna has spent baking in the oven.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
