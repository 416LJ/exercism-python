def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    steps = 0
    while number != 1:
        steps += 1
        if number % 2 == 0:
            number = number/2
        else:
            number = (number*3) + 1
        print(number)
    return steps

print(steps(45))