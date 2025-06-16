def rebase(input_base, digits, output_base):
    check_input_base = input_base >= 2
    check_output_base = output_base >= 2
    
    if not check_input_base or not check_output_base:
        if not check_input_base:
            print("input less than 2")
            raise ValueError("input base must be >= 2")
        elif not check_output_base:
            raise ValueError("output base must be >= 2")
        elif not check_input_base and not check_output_base:
            print("both negative bases")
            raise ValueError("all digits must satisfy 0 <= d < input base")
        
    for number in digits:
        if number >= 0 and number < input_base:
            continue
        else:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    
    if len(digits) == 0:
        digits.append(0)
        return digits
    elif sum(digits) == 0:
        digits.clear()
        digits.append(0)
        return digits
    
    temp_digits = []
    temp_10 = 0
    
    digits.reverse()

    counter = 0
    for number in digits:
        temp_digits.append(number*(input_base ** counter))
        counter += 1

    temp_10 = sum(temp_digits)
    final_list = []

    def converter(temp_digits,output_base):
        quotient = temp_10
        quotient_2 = temp_10
        remainder = 0
        while quotient > 0:
            quotient = quotient // output_base
            remainder = quotient_2 % output_base
            quotient_2 = quotient
            final_list.append(remainder)

        return final_list

    final_list = converter(temp_digits,output_base)
    final_list.reverse()
    return final_list


