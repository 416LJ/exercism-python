def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    total = []
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        for i in range(2,number+1):
            if number % i == 0:
                total.append(number/i)
        total = sum(total)
        if total > number:
            return "abundant"
        elif total < number:
            return "deficient"
        else:
            return "perfect"


print(classify(15))
print(classify(6))
print(classify(28))
print(classify(16))

