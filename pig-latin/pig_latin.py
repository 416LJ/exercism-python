chars = {
    "vowels":["a","e","i","o","u"],
    "cons": ['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
}

test_text = "therapy"
new_words = []
def translate(text):
    text = text.split()
    new_words = []
    
    for word in text:
        count = 0
        if word[0] in chars['vowels'] or word.startswith(('xr','yt','ay')):
            word = word+"ay"
            new_words.append(word)
        elif "y" in word and not word.startswith("y") and not word.startswith("th"):
            inx_val = word.index("y")
            suffix = word[:inx_val]
            prefix = word[inx_val:]
            new_words.append(prefix+suffix+"ay")
            print(word)
        elif word[0] in chars['cons'] or word.startswith("qu") or "qu" in word:
            if word.startswith("qu") or "qu" in word:
                for letter in word:
                    if count <1:
                        if letter in chars["vowels"]:
                            if word[word.index(letter)+1] == "q":
                                count += 1
                                suffix = word[:word.index(letter)]
                                prefix = word[word.index(letter):]
                                new_words.append(prefix+suffix+"ay")

                            else:
                                count += 1
                                inx_val = word.index("qu")+2
                                suffix = word[:inx_val]
                                prefix = word[inx_val:]
                                new_words.append(prefix+suffix+"ay")

            else:
                for letter in word:   
                    if count <1:
                        if letter in chars["vowels"]:
                            if word.startswith("th") and word[2] in chars["vowels"]:
                                count += 1

                                if word[word.index(letter)] in chars["vowels"]:
                                    suffix = word[:word.index(letter)]
                                    prefix = word[word.index(letter):]
                                    new_words.append(prefix+suffix+"ay")
                                    

                            else:
                                count += 1
                                inx_val = (word.index(letter))
                                suffix = word[:inx_val]
                                prefix = word[inx_val:]
                                word = prefix+suffix+"ay"

                                new_words.append(word)

        
    return  " ".join(new_words)
    

    
   


# iquidlay
# erapythay
print(translate(test_text))