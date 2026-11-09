"""
Sentence scrambler: turns readable text into gibberish that can be reversed
with the same key.

Scrambling happens in two steps:
1. Each letter is shifted through the alphabet by the matching letter of the
   key (a Vigenere cipher). Case is preserved and non-letters are untouched.
2. Every character is rearranged with a rail fence (zigzag) transposition,
   which also hides where the spaces and punctuation were.

Unscrambling runs the same two steps in reverse order:
1. Undo the rail fence: _rail_fence_order(len(text)) lists the original
   position of each scrambled character, so put each one back where it came from.
2. Undo the letter shift with _shift_letters(text, _key_shifts(key), -1).

For example, with the default key:
    scramble("Hello world, meet me at noon!")    -> "Rvb g u!mn bt,oi mt sxeawlwvb"
    unscramble("Rvb g u!mn bt,oi mt sxeawlwvb")  -> "Hello world, meet me at noon!"
"""

DEFAULT_KEY = "kitchen"
_RAILS = 3


def _key_shifts(key):
    """Validate the key and convert its letters into shift amounts (a=0 ... z=25)."""
    if not isinstance(key, str):
        raise TypeError("key must be a string")
    shifts = [ord(ch) - ord("a") for ch in key.lower() if "a" <= ch <= "z"]
    if not shifts:
        raise ValueError("key must contain at least one letter a-z")
    return shifts


def _shift_letters(text, shifts, direction):
    """Shift each letter of text by the repeating key shifts (direction is 1 or -1)."""
    result = []
    letter_index = 0
    for ch in text:
        if "a" <= ch.lower() <= "z":
            base = ord("A") if ch.isupper() else ord("a")
            amount = direction * shifts[letter_index % len(shifts)]
            result.append(chr((ord(ch) - base + amount) % 26 + base))
            letter_index += 1
        else:
            result.append(ch)
    return "".join(result)


def _rail_fence_order(length):
    """Return the original positions in the order the rail fence reads them out."""
    zigzag = list(range(_RAILS)) + list(range(_RAILS - 2, 0, -1))
    rows = [zigzag[i % len(zigzag)] for i in range(length)]
    return sorted(range(length), key=lambda i: rows[i])


def scramble(text, key=DEFAULT_KEY):
    """
    Scramble text into unreadable gibberish.

    Args:
        text: The message to scramble.
        key: Secret word used to scramble the message. Only someone with the
            same key can unscramble it. Must contain at least one letter.

    Returns:
        The scrambled message, the same length as the original.

    Raises:
        TypeError: If text or key is not a string.
        ValueError: If key contains no letters.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    shifts = _key_shifts(key)
    shifted = _shift_letters(text, shifts, 1)
    return "".join(shifted[i] for i in _rail_fence_order(len(shifted)))

"""
Sentence unscrambler: turns gibberish that is a result of the sentence scrambler into readable English text.
This is done via using the same map that sentence scrambler uses. 
This does not magically unscramble random text that was not created using the scrambler above.
"""

def unscramble(text, key=DEFAULT_KEY):
    """
    Restore text scrambled with the same key.

    Args:
        text: The scrambled message.
        key: The key originally used to scramble the message.

    Returns:
        The restored message, the same length as the scrambled text.

    Raises:
        TypeError: If text or key is not a string.
        ValueError: If key contains no letters.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    shifts = _key_shifts(key)

    restored = [""] * len(text)
    for character, original_position in zip(
        text, _rail_fence_order(len(text))
    ):
        restored[original_position] = character

    return _shift_letters("".join(restored), shifts, -1)