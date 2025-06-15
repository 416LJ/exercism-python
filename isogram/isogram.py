import string
def is_isogram(string):
    chars = []
    copy_word = []
    if string == "":
        return True
    else:
        word = string.lower()
        word = sorted(list(word.replace(' ','')))
        print(word)
        for letter in (word):
            if not letter.isalnum():
                chars.append(letter)
            else:
                copy_word.append(letter)
        copy_word = sorted(list(set(copy_word))+chars)
        return copy_word == word




print(is_isogram("six-year-old"))
