"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    c1 = (str(list_one).strip("[]") + ",")
    c2 = (str(list_two).strip("[]") + ",")

    if list_one == list_two:
        return 3
    elif c1 in c2:
        return 1
    elif c2 in c1:
        return 2
    else:
        return 4
        





print(sublist([0, 1, 2], [0, 1, 2, 3, 4, 5]))

