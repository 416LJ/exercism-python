def leap_year(year):
    if year % 4 == 0:
        print("divisible by 4", year)
        if year % 100 == 0:
            print("divisible by 4 and 100", year)
            if year % 400 == 0:
                print("divisible by 4 ,100, 400", year)
                return True
            else:
                print("not divisible by 400", year)
                return False
        else:
            print("divisible by 100", year)
            return True
    else:
        print("not divisible by 4", year)
        return False

print(leap_year(1800))
print(leap_year(1900))
print(leap_year(1997))
