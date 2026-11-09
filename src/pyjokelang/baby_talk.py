# baby talk function turns regular words into baby talk by changing
# the letters to phonetically match how baby talk sounds

"""Baby Talk - Turns normal english into how a baby speaks"""

def babytalk(normal_phrase):
    """Converts a normal phrase to baby talk"""
    # converts r to l
    baby_phrase = ""
    for char in normal_phrase:
        if char=="r":
            baby_phrase+="w"
        elif char == "R":
            baby_phrase+= "W"
        else:
            baby_phrase += char
    return baby_phrase
