import random


def random_caps(text):
    """Randomly uppercase or lowercase each letter in a string."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return "".join(
        random.choice((character.lower(), character.upper()))
        if character.isalpha() else character
        for character in text
    )
