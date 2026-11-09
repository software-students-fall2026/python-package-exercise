'''
English to pig latin:
'''

def english_to_pig_latin(text):
    """
    Translate English text into Pig Latin.

    Words starting with a vowel get "way" added to the end. Otherwise the
    leading consonants move to the end of the word, followed by "ay".
    The output is all lowercase.
    """
    vowels = "aeiou"
    words = text.lower().split()
    translated_words = []
    for word in words:
        if word[0] in vowels:
            pig_latin_word = word + "way"
        else:
            index = 0
            while index < len(word) and word[index] not in vowels:
                index += 1
            pig_latin_word = word[index:] + word[:index] + "ay"
        translated_words.append(pig_latin_word)
    return " ".join(translated_words)

    #RYTHM
    # YTHMR-AY
    #APPLE
    # PPLEA-WAY
    #ART
    # RTA-WAY

