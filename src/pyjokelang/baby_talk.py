# baby talk function turns regular words into baby talk by changing
# the letters to phonetically match how baby talk sounds

def babytalk(normal_phrase):
    # converts r to l
    baby_phrase = ""
    for char in normal_phrase:
        if char=="r":
            baby_phrase+="w"
        elif char == "R":
            baby_phrase+= "W"
        else:
            baby_phrase += char
    return(baby_phrase)