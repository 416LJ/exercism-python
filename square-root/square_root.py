"""

Set a number and try it out

"""
number = 9999*9999

def square_root(number):
    if number == 1:
        return 1
    
    iterations = 0
    left = 2
    right = number-1

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if mid*mid == number:
            print(f"found sq rt of {number} : {mid} in {iterations} attempts")
            return mid
        
        elif mid*mid < number:
            left = mid + 1

        else:
            right = mid - 1

def square_root2(number):
    iterations = 0
    for i in range(1,number):
            iterations += 1
            if i*i == number:
                return f"found sq rt of {number} : {i} in {iterations} attempts"
            

square_root(number)
print(square_root2(number))
