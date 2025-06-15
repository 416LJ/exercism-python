def is_valid(isbn):
    cleaned = isbn.upper().replace('-','')
    if len(cleaned) == 10:
        if cleaned[0:-1].isnumeric():
            if cleaned[-1].isnumeric() or cleaned[-1] == "X":
                d = list(cleaned)
                if d[-1] == "X":
                    d[-1] = 10
                    d = [int(x) for x in d]
                    return (d[0] * 10 + d[1] * 9 + d[2] * 8 + d[3] * 7 + d[4] * 6 + d[5] * 5 + d[6] * 4 + d[7] * 3 + d[8] * 2 + d[9] * 1) % 11 == 0
                else:
                    d = [int(x) for x in d]
                    return (d[0] * 10 + d[1] * 9 + d[2] * 8 + d[3] * 7 + d[4] * 6 + d[5] * 5 + d[6] * 4 + d[7] * 3 + d[8] * 2 + d[9] * 1) % 11 == 0
            else:
                return False
        else:
            return False
    else:
        return False


print(1,is_valid("3598215088"))
print(2,is_valid("3-598-21507-X"))
print(3,is_valid("3-598-2X507-9"))
print(4,is_valid("3-598-21507-X"))
print(5,is_valid("3-598-21507-A"))
print(6,is_valid("00"))