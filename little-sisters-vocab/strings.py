"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    prefix = 'un'
    print("hello")
    return prefix + word

    


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    prefix = [vocab_words[0]]
    for i in range(1,len(vocab_words)):
        prefix.append(prefix[0]+vocab_words[i])
    prefix = ' :: '.join(prefix)
    return prefix

def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    suffix = word[-4:]
    if suffix in word:
        word = word.removesuffix(suffix)
        if word[-1] == 'i':
            word = word.removesuffix('i')
            return word+"y"
        else:
            return word


        


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    sentence = sentence.split()
    suffix = 'en'
    if sentence[index][-1] == '.':
        sentence[index] = sentence[index].removesuffix('.')
    return sentence[index]+suffix



print(adjective_to_verb('I need to make that bright.', -1 ))
print(adjective_to_verb("It got dark as the sun set.", 2))
