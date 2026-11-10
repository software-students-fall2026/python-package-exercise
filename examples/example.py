"""
Example program that demonstrates every function in pyjokelang.

Run it from the project root with:
    pipenv run python examples/example.py
"""

from pyjokelang import scramble, unscramble


def scramble_example():
    """Show scramble() and unscramble(), with the default key and a secret key."""
    print("=== Scramble and unscramble ===")
    message = "Meet me at noon!"
    print(f"Original message:          {message}")

    # with the default key, anyone with pyjokelang can unscramble it
    scrambled = scramble(message)
    print(f"Scrambled (default key):   {scrambled}")
    print(f"Unscrambled:               {unscramble(scrambled)}")

    # with a secret key, only someone who knows the key can unscramble it
    secret = scramble(message, key="tacos")
    print(f"Scrambled (key 'tacos'):   {secret}")
    print(f"Unscrambled with 'tacos':  {unscramble(secret, key='tacos')}")
    print(f"Unscrambled with 'pizza':  {unscramble(secret, key='pizza')}")
    print()


def main():
    """Run every example."""
    scramble_example()


if __name__ == "__main__":
    main()
