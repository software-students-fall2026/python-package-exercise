'''
English to pig latin:

Move the first letter to the end of the word and add -ay. 

Unless the first letter is a vowel, then keep the word unchanged and add -ay.

If the word ends in a vowel add -way instead.

Use a helper function to reverse capital and lowercase letters. 

Use a helper function to scramble punctuation.

Use a helper function to translate full sentences.

KNOWN ISSUE: For words with W, the pig latin to english doesn't work 

(ex hello world -> ellohay orldway -> hello orld). 

PROPOSED SOLUTION: Add dashes so we know where to split

'''

def english_word_to_pig_latin(text):
    """Translate a single English word into Pig Latin."""
    vowels = "aeiou"
    word = text.lower()
    # if the first letter is a vowel, keep that here
    if word[0] in vowels:
        pig_latin_word = word + "-way"
    # if it's not a vowel, then add the first letter to the end and add ay
    else:
        pig_latin_word = word[1:] + word[0] + "-ay"
    return pig_latin_word

def english_sentence_to_pig_latin(text):
    """Translate an entire English sentence into Pig Latin."""
    translated_words = []
    words = text.lower().split()
    for word in words:
        translated_words.append(english_word_to_pig_latin(word))
    return " ".join(translated_words)

def reverse_capitalization():
    """This will turn all capital letters into lowercase and vice versa."""



def reverse_punctuation():
    """This will turn exclamation points into periods, turn periods into question marks."""


def pig_latin_word_to_english(text):
    """Translate a single Pig Latin word back into English."""
    word = text.lower()

    # if it ends in "-way", the word started with a vowel, so just remove the "-way"
    if word.endswith("-way") and len(word) > 4:
        return word[:-4]
    # otherwise remove the "-ay" and move the last letter back to the front
    if word.endswith("-ay") and len(word) > 3:
        stem = word[:-3]
        return stem[-1] + stem[:-1]
    # anything else isn't Pig Latin, so leave it unchanged
    return word


def pig_latin_sentence_to_english(text):
    """Translate a full Pig Latin sentence back into English."""
    translated_words = []
    words = text.lower().split()
    for word in words:
        translated_words.append(pig_latin_word_to_english(word)) #call helper

    return " ".join(translated_words)
