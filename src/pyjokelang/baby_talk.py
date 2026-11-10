# baby talk function turns regular words into baby talk by changing
# the letters to phonetically match how baby talk sounds

"""Baby Talk - Turns normal english into how a baby speaks"""

# Intensity Level 0: ONLY swaps letters, not full words
letter_swap = {"r":"w", "l":"w", "v":"b"}

#Intensity Level 1: swaps letters AND full words
keyword_swap = {
    "hello": "hewwo",
    "please": "pwease",
    "water": "wawa",
    "mother": "mama",
    "father": "dada"}

#Intensity Level 2: swaps letters AND full words AND "extreme" letters

MAX_letter_swap = {"r":"w", "l":"w", "v":"b", "th": "d", "ch": "t"}


def babytalk(normal_phrase, intensity):
    """Converts a normal phrase to baby talk: r -> w, l -> w, v -> b"""

    baby_phrase = ""

    if intensity==1:
        for char in normal_phrase:
            if char in letter_swap:
                baby_phrase+=letter_swap[char]
            else:
                baby_phrase += char
        return baby_phrase
