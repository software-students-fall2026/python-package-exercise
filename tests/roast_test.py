import pytest
from pyroast import pyroast

class Test:
    # GPA roast
    def test_roast_gpa(self):
        '''
        Verify roast_gpa() returns a non-empty string.
        '''
        actual = pyroast.roast_gpa(3.86)
        assert isinstance(actual, str), f"Expected roast_gpa() to return a string. Instead, it returned {actual}"
        assert len(actual) > 0, f"Expected roast_gpa() not to be empty. Instead, it returned a string with {len(actual)} characters"
    # Height roast
    def test_roast_height(self):
        """
        Verify roast_height() returns a non-empty string.
        """
        actual = pyroast.roast_height(6.0)
        assert isinstance(actual, str), f"Expected roast_height() to return a string. Instead, it returned {actual}"
        assert (len(actual) > 0), f"Expected roast_height() not to be empty. Instead, it returned a string with {len(actual)} characters"

    def test_roast_height_thresholds(self):
        """
        Verify roast_height() across different height thresholds.
        """
        sample_heights = [7.0, 6.7, 6.4, 6.1, 5.9, 5.0, 3.0]
        for h in sample_heights:
            actual = pyroast.roast_height(h)
            assert isinstance(actual, str), f"Expected string for height {h}, got {type(actual)}"
            assert (len(actual) > 0), f"Expected non-empty string for height {h}, got empty string"

    def test_roast_height_type(self):
        """
        Verify return type is a string.
        """
        actual = pyroast.roast_height(6.0)
        assert isinstance(actual, str), f"Expected string, got {type(actual)}"

    # Coffee roast
    def test_roast_coffee(self):
        """
        Verify roast_coffee() returns a non-empty string.
        """
        actual = pyroast.roast_coffee(3)
        assert isinstance(actual, str), f"Expected string, got {type(actual)}"
        assert len(actual) > 0, "Expected a non-empty string"

    def test_roast_coffee_thresholds(self):
        """
        Verify roast_coffee() across different coffee thresholds.
        """
        sample_cups = [0, 1, 2, 3, 4, 5, 10]
        for cups in sample_cups:
            actual = pyroast.roast_coffee(cups)
            assert isinstance(actual, str), f"Expected string for {cups} cups"
            assert len(actual) > 0, f"Expected non-empty string for {cups} cups"

    def test_roast_coffee_espresso(self):
        """
        Verify high coffee consumption returns the espresso roast.
        """
        actual = pyroast.roast_coffee(6)
        assert actual == "Your blood has turned into espresso."