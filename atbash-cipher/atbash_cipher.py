plain = list("abcdefghijklmnopqrstuvwxyz1234567890")
cypher = list("zyxwvutsrqponmlkjihgfedcba1234567890")
translator = {plain[i] :  cypher[i] for i in range(len(plain))}

def encode(plain_text):
    temp = list(plain_text.lower().replace(" ", ""))
    encoded = []
    encoded_str = ""
    for i in temp:
        if i.isalnum():
            encoded.append(translator[i])

    print(encoded)
    encoded_str = [''.join(encoded[variable:variable+5]) for variable in range(0, len(encoded),5)]
    encoded_str = ' '.join(encoded_str)
    #print(encoded_str)
    return encoded_str

def decode(ciphered_text):
    temp = list(ciphered_text.lower().replace(" ", ""))
    encoded = []
    encoded_str = ""
    for i in temp:
        if i.isalnum():
            encoded.append(translator[i])

    print(encoded)
    encoded_str = [''.join(encoded[variable:variable+5]) for variable in range(0, len(encoded),5)]
    encoded_str = ' '.join(encoded_str)
    #print(encoded_str)
    return encoded_str.replace(" ","")

