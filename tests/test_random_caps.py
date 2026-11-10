"""Tests for random capitalization."""

from unittest.mock import patch

import pytest

from pyjokelang.random_caps import random_caps


class Tests:
    """Unit tests for random_caps()."""

    def test_lowercase_output(self):
        """Selecting the lowercase option lowercases every letter."""
        with patch(
            "pyjokelang.random_caps.random.choice",
            side_effect=lambda options: options[0],
        ):
            actual = random_caps("HeLLo, WORLD! 123")
            expected = "hello, world! 123"
            assert actual == expected, (
                f"Expected '{expected}'. Instead, it returned '{actual}'"
            )

    def test_uppercase_output(self):
        """Selecting the uppercase option uppercases every letter."""
        with patch(
            "pyjokelang.random_caps.random.choice",
            side_effect=lambda options: options[1],
        ):
            actual = random_caps("Hello, world! 123")
            expected = "HELLO, WORLD! 123"
            assert actual == expected, (
                f"Expected '{expected}'. Instead, it returned '{actual}'"
            )

    def test_mixed_output(self):
        """Each letter receives its own capitalization choice."""
        with patch(
            "pyjokelang.random_caps.random.choice",
            side_effect=["a", "B", "c", "D"],
        ) as choose:
            actual = random_caps("Ab cD!")
            assert actual == "aB cD!", (
                f"Expected 'aB cD!'. Instead, it returned '{actual}'"
            )
            assert choose.call_count == 4, (
                "Expected one random choice for each of the four letters"
            )

    def test_edge_inputs(self):
        """Empty text, numbers, punctuation, and whitespace stay unchanged."""
        with patch("pyjokelang.random_caps.random.choice") as choose:
            assert random_caps("") == "", "Expected an empty string"
            assert random_caps("123 !?") == "123 !?", (
                "Expected numbers and punctuation to stay unchanged"
            )
            assert random_caps(" \n\t") == " \n\t", (
                "Expected whitespace to stay unchanged"
            )
            choose.assert_not_called()

    def test_invalid_inputs(self):
        """Inputs that are not strings raise TypeError."""
        with pytest.raises(TypeError):
            random_caps(123)
        with pytest.raises(TypeError):
            random_caps(None)
        with pytest.raises(TypeError):
            random_caps([])
        with pytest.raises(TypeError):
            random_caps({})
