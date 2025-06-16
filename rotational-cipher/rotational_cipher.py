import re

def rotate(text, key):
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', ' ', text)

    normal = list("abcdefghijklmnopqrstuvwxyz")

    if key == 0 or key == 26:
        return cleaned_text
    else:

        key = key % len(normal)
        shifted = normal[key:] + normal[:key]
        shifted_words = []

        for i in text:
            if i.isnumeric() or i == " ":
                shifted_words.append(i)
            else:
                if not i.isalnum():
                    shifted_words.append(i)
                elif i.isupper():
                    i = i.lower()
                    shifted_words.append(shifted[normal.index(i)].upper())
                    pass
                else:
                    shifted_words.append(shifted[normal.index(i)])
           
        shifted_words = "".join(shifted_words)
        return shifted_words


rotate("Let's eat, Grandma!", 21)
# ("Let's eat, Grandma!", 21), "Gzo'n zvo, Bmviyhv!")