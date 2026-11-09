'''
English to pig latin:

Move the first letter to the end of the word and add -ay. 

Unless the first letter is a vowel, then keep the word unchanged and add -ay.

If the word ends in a vowel add -way instead.

Use a helper function to reverse capital and lowercase letters. 

Use a helper function to scramble punctuation.

Use a helper function to translate full sentences.

'''

def english_word_to_pig_latin(text):
    vowels = "aeiou"
    word = text.lower()

    # if the first letter is a vowel, keep that here
    if word[0] in vowels:
        pig_latin_word = word + "way"
    # if it's not a vowel, then add the first letter to the end and add ay 
    else:
        pig_latin_word = word[1:] + word[0] + "ay"

    return pig_latin_word



'''
helper to make the entire sentence piglatin, not just words
'''
def english_sentence_to_piglatin(text):
    translated_words = []
    words = text.lower().split()
    for word in words:
        translated_words.append(english_word_to_pig_latin(word))

    return " ".join(translated_words)