"""Tests for the sentence scrambler."""

import pytest

from pyjokelang.scrambler import scramble


class Tests:
    """Unit tests for scramble()."""

    def test_known_output(self):
        """Scrambling known input with a known key gives the expected output."""
        message = "Hello world, meet me at noon!"
        actual = scramble(message)
        expected = "Rvb g u!mn bt,oi mt sxeawlwvb"
        assert actual == expected, (
            f"Expected '{expected}' with the default key. Instead, it returned '{actual}'"
        )

        # key "b" shifts each letter by 1 -> "bcde"; zigzag rows 0,1,2,1 -> "b" "ce" "d"
        actual = scramble("abcd", key="b")
        assert actual == "bced", f"Expected 'bced'. Instead, it returned '{actual}'"

        # default key starts with "k", which shifts a single letter by 10
        actual = scramble("a")
        assert actual == "k", (
            f"Expected a single letter to be shifted to 'k'. Instead, it returned '{actual}'"
        )

        # a key longer than the message only uses its first letters: "a" (+0), "b" (+1)
        actual = scramble("hi", key="abcdefghijklmnop")
        assert actual == "hj", (
            f"Expected 'hj' with a key longer than the message. Instead, it returned '{actual}'"
        )

    def test_unreadable_and_deterministic(self):
        """Output differs from the input, keeps its length, and never changes between runs."""
        message = "The quick brown fox jumps over the lazy dog"
        actual = scramble(message)
        assert actual != message, "Expected the scrambled text to differ from the original"
        assert len(actual) == len(message), (
            f"Expected length {len(message)}. "
            f"Instead, it returned a string with {len(actual)} characters"
        )
        assert scramble(message) == actual, (
            "Expected scrambling the same text twice to give the same result"
        )

    def test_key_changes_output(self):
        """Different keys give different results; the default key is 'kitchen'."""
        message = "meet me at noon"
        assert scramble(message, key="tacos") != scramble(message, key="pizza"), (
            "Expected different keys to give different scrambled text"
        )
        assert scramble(message) == scramble(message, key="kitchen"), (
            "Expected the default key to be 'kitchen'"
        )
        assert scramble(message, key="KITCHEN") == scramble(message, key="kitchen"), (
            "Expected keys to be case-insensitive"
        )
        assert scramble(message, key="a1b!") == scramble(message, key="ab"), (
            "Expected non-letter characters in the key to be ignored"
        )

    def test_edge_inputs(self):
        """Empty text, text with no letters, and mixed case are handled."""
        actual = scramble("")
        assert actual == "", f"Expected an empty string. Instead, it returned '{actual}'"

        no_letters = "123 !?"
        actual = scramble(no_letters)
        assert sorted(actual) == sorted(no_letters), (
            f"Expected text with no letters to only be rearranged. Instead, it returned '{actual}'"
        )

        mixed = "HeLLo WoRLD"
        actual = scramble(mixed)
        expected_upper = sum(ch.isupper() for ch in mixed)
        actual_upper = sum(ch.isupper() for ch in actual)
        assert actual_upper == expected_upper, (
            f"Expected {expected_upper} uppercase letters. Instead, '{actual}' has {actual_upper}"
        )

    def test_invalid_inputs(self):
        """Bad text or key types and keys without letters raise errors."""
        with pytest.raises(TypeError):
            scramble(123)
        with pytest.raises(TypeError):
            scramble(None)
        with pytest.raises(TypeError):
            scramble("hello", key=42)
        with pytest.raises(ValueError):
            scramble("hello", key="")
        with pytest.raises(ValueError):
            scramble("hello", key="123")
