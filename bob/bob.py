def response(hey_bob):
    print(len(hey_bob))
    if len(hey_bob.strip()) == 0:
        return "Fine. Be that way!"
    hey_bob = hey_bob.strip()
    if hey_bob.isupper():
        if hey_bob[-1] == "?":
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif hey_bob[-1] == "?":
        return "Sure."
    else:
        return "Whatever."

print(response("123    "))

def response2(hey_bob):
    hey_bob = hey_bob.strip()
    print(len(hey_bob))
    if not hey_bob:
        return 'Fine. Be that way!'
    elif hey_bob[-1] == '?':
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return 'Sure.'
    elif hey_bob.isupper():
        print("all upper", hey_bob)
        return 'Whoa, chill out!' 
    else:
        return 'Whatever.'
    
print("123" == "123".upper())
print(response2("123    "))