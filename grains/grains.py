def square(number):
    grains_sqaures = {}
    sqaures = 1
    grains = 1

    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    for i in range(0,65):
        if i > 1:
            grains = grains*2
            sqaures += 1
        grains_sqaures[sqaures] = grains
    return grains_sqaures.get(number)


def total():
    return 2**64-1


