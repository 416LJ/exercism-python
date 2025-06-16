import math

def score(x, y):
    res = math.hypot(x, y)
    if res <= 10:
        if x >= 10 or x <= -10 or y >= 10 or y <= -10:
            return 1
        elif x > 5 or x < -5 or y > 5 or y< -5:
            return 1
        elif x > 1 or x < -1 or y > 1 or y < -1:
            if res > 5:
                return 1
            else:
                return 5
        elif x < 1 or x > -1 or y < 1 or y > -1:
            if res > 1:
                return 5
            else:
                return 10
    else:
        return 0


print(score(-3.6,-3.6))



print(math.hypot(-3.6, -3.6))


