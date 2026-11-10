# pyjokelang

Translate English into silly joke languages like Pig Latin and Baby Talk, and back again. Also translate any language into a random text of the same length, and back again. 

## Setup

From the project root, install [pipenv](https://pipenv.pypa.io/) and then run:

```bash
pipenv install --dev
```
## Pig Latin rules
 
> Confirm with Jade in order to ensure our methods match each other and follow the same rules
 
`to_pig_latin` and `from_pig_latin` follow these rules, so any text translated into Pig Latin can be translated back.
 
### Translating English to Pig Latin
 
The vowels are a, e, i, o and u. **Y never counts as a vowel.**
 
1. **Words starting with a consonant:** Move the first letter to the end of the word and add -ay.
2. **Words starting with a vowel:** Keep the word unchanged and add -way.
3. **Capitals:** The word translator preserves the original capitalization of letters, while the sentence translator reverses uppercase and lowercase letters using the reverse_capitalization() helper.
4. **Punctuation:** The sentence translator uses reverse_punctuation() to change ! to ., . to ?, and ? to !. Other characters remain unchanged.
5. **Full Sentences:** Split the sentence into individual words, translate each word into Pig Latin, join the translated words with spaces, and apply the capitalization and punctuation helpers.
6. **Whitespace:** Multiple spaces between words are reduced to single spaces. Empty sentences return an empty string.


### Translating Pig Latin back to English
 
**Finding translated words:** a translated word has letters containing at least one vowel, then a dash, then any moved letters, then `ay`. Anything else stays unchanged.
 
For each translated word:
 
1. **Remove only the final `ay`** (or `AY`) after the dash. Any "ay" before the dash belongs to the word, so `ay-way` becomes `way`.
2. **Move the letters back:** put the letters between the dash and the final `ay` in front of the letters before the dash, and remove the dash. If there are no letters between them, the word started with a vowel, so just remove `-ay`.
3. **Restore the capitalization** using the first matching rule:
   - **All caps:** if the whole word is in capitals, keep the whole result in capitals.
   - **Capitalized:** if only the first letter is a capital, make that letter lowercase and capitalize the new first letter of the word. If "qu" moved back, only the `q` becomes a capital.
   - **Lowercase:** keep the whole result in lowercase.
   
| Pig Latin | English | What happens |
|---|---|---|
| ing-stray | string | `str` moves back in front of `ing` |
| es-yay | yes | a moved `y` goes back to the front like any consonant |
| apple-ay | apple | no moved letters, so only `-ay` is removed |
| ay-way | way | only the final `ay` is removed |
| Ello-hay | Hello | `E` becomes lowercase and `h` becomes a capital |
| ELLO-HAY | HELLO | everything stays in capitals |
| Apple-ay | Apple | the first letter doesn't change, so it stays a capital |
| I-ay | I | a single-letter word keeps its capital |
| Iet-quay | Quiet | `I` becomes lowercase and only `q` becomes a capital |

## Scramble and unscramble

`scramble` turns any text into unreadable gibberish, and `unscramble` turns it back. Share the scrambled text with a friend, and they can unscramble it on their own machine. Add a secret `key` and only someone who knows the key can read it.

```python
from pyjokelang import scramble, unscramble

scramble("Hello world, meet me at noon!")
# 'Rvb g u!mn bt,oi mt sxeawlwvb'

unscramble("Rvb g u!mn bt,oi mt sxeawlwvb")
# 'Hello world, meet me at noon!'

secret = scramble("Meet me at noon!", key="tacos")
# 'F agehe vbh!gx n'

unscramble(secret, key="tacos")
# 'Meet me at noon!'

unscramble(secret, key="pizza")   # wrong key, still gibberish
# 'Qwhi ei sw cgsf!'
```

### `scramble(text, key="kitchen")`

Scrambles `text` and returns the result. The output is always the same length as the input, and the same text and key always give the same output.

| Argument | Description |
|---|---|
| `text` | The message to scramble. |
| `key` | Optional secret word. Only its letters are used, and it isn't case-sensitive, so `"Tacos!"` works the same as `"tacos"`. Defaults to `"kitchen"`. |

### `unscramble(text, key="kitchen")`

Turns text made by `scramble` back into the original message. Use the same `key` that was used to scramble it; a different key gives gibberish.

| Argument | Description |
|---|---|
| `text` | The scrambled message. |
| `key` | The key used to scramble the message. Defaults to `"kitchen"`. |

### Errors

Both functions raise:

- `TypeError` if `text` or `key` isn't a string
- `ValueError` if `key` has no letters, for example `""` or `"123"`

### How it works

Scrambling happens in two steps:

1. **Shift the letters.** Each letter moves forward through the alphabet by the matching letter of the key (a = 0, b = 1, …, z = 25), repeating the key as needed. This is a [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher). Capital letters stay capital, and everything else is left as it is.
2. **Rearrange every character.** Characters are written in a zigzag across 3 rows and read off row by row. This is a [rail fence cipher](https://en.wikipedia.org/wiki/Rail_fence_cipher), and it hides where the spaces and punctuation were.

`unscramble` undoes the two steps in reverse order.

### From the command line

```bash
pyjokelang scramble 'Meet me at noon!' --key tacos
pyjokelang unscramble 'F agehe vbh!gx n' --key tacos
```

See [`examples/example.py`](./examples/example.py) for a complete program.

## Team Members
- [Jade Leong](https://github.com/jade-leong)
- [Risha Chada](https://github.com/rishachada)
- [Sanjana Chauhan](https://github.com/schauhans)
- [Seth DeRusha](https://github.com/sethderusha)
- [Yufei Huang](https://github.com/yufeiihuang)