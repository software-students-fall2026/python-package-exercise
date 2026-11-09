'''
English to pig latin:

Move the first letter to the end of the word and add -ay. 

Unless the first letter is a vowel, then keep the word unchanged and add -ay.

If the word ends in a vowel add -way instead.

Use a helper function to reverse capital and lowercase letters. 

Use a helper function to scramble punctuation.

'''
def english_to_pig_latin(text):
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