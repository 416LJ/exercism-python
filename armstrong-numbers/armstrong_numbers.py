def is_armstrong_number(number):
    numbers = list(str(number))
    total = 0
    for i in numbers:
        total += int(i)**len(numbers)
    return total == number
