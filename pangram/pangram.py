import string

def is_pangram(sentence):
    alphabets = string.ascii_lowercase[:26]
    sentence = sentence.lower()
    sentence = list(sentence.replace(' ',''))
    return all(item in sentence for item in alphabets)

print(is_pangram("hello world"))

