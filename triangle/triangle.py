
        def equilateral(sides):
    if 0 in sides:
        return False
    else:
        return len(set(sides)) == 1

def isosceles(sides):
    if sides[0] + sides[1] <= sides[2]:
        return False
    if sides[1] + sides[2] <= sides[0]:
        return False
    if sides[0] + sides[2] <= sides[1]:
        return False
    

    if sides[0] == sides[1]:
        return True
    if sides[1] == sides[2]:
        return True
    if sides[0] == sides[2]:
        return True
    

    return False
    

def scalene(sides):
    if sides[0] + sides[1] <= sides[2]:
        return False
    if sides[1] + sides[2] <= sides[0]:
        return False
    if sides[0] + sides[2] <= sides[1]:
        return False
    

    if len(set(sides)) == 3:
        return True
    
    return False




print(isosceles([3, 4, 4]))
print(scalene([0.5, 0.4, 0.6]))
