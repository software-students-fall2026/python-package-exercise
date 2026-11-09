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

    def test_roast_gpa_thresholds(self):
        '''
        Verify roast_gpa() across various thresholds
        '''
        sample_gpa = [1.0, 2.6, 2.9, 2.0, 3.6, 4.0]
        for g in sample_gpa:
            actual = pyroast.roast_gpa(g)
            assert isinstance(actual, str), f"Expected roast_gpa() to return a string for gpa {g}. Instead, it returned {actual}"
            assert len(actual) > 0, f"Expected roast_gpa() not to be empty for gpa {g}. Instead, it returned a string with {len(actual)} characters"

    def test_roast_gpa_sleep(self):
        '''
        Verify roast_gpa() returns the expected message for a gpa higher than or equal to 3.9
        '''
        actual = pyroast.roast_gpa(4.0)
        assert actual == "I bet you've never known sleep before"

    
    def test_roast_gpa_smell(self):
        '''
        Verify roast_gpa() returns the expected message for a gpa higher than or equal to 3.5
        '''
        actual = pyroast.roast_gpa(3.6)
        assert actual == "I smell wasted potential"

    def test_roast_gpa_network(self):
        '''
        Verify roast_gpa() returns the expected message for a gpa higher than or equal to 3.0
        '''
        actual = pyroast.roast_gpa(3.1)
        assert actual == "Are you even trying? Or is college just a networking event for you?"

    def test_roast_gpa_quit(self):
        '''
        Verify roast_gpa() returns the expected message for a gpa higher than or equal to 2.5
        '''
        actual = pyroast.roast_gpa(2.6)
        assert actual == "At this point, it might be better to give up"

    def test_roast_gpa_choice(self):
        '''
        Verify roast_gpa() returns the expected message for a gpa higher than or equal to 2.0
        '''
        actual = pyroast.roast_gpa(2.1)
        assert actual == "I see you gave up, smartest choice you've ever made"

    def test_roast_gpa_drop(self):
        '''
        Verify roast_gpa() returns the expected message for a gpa higher than or equal to 1.5
        '''
        actual = pyroast.roast_gpa(1.9)
        assert actual == "Gonna drop out soon?"

    def test_roast_gpa_low(self):
        '''
        Verify roast_gpa() returns the expected message for a gpa higher than or equal to 1.0
        '''
        actual = pyroast.roast_gpa(1.1)
        assert actual == "McDonalds is always hiring"

    def test_roast_gpa_lower(self):
        '''
        Verify roast_gpa() returns the expected message for a gpa higher than or equal to 0.5
        '''
        actual = pyroast.roast_gpa(0.9)
        assert actual == "Your GPA is lower than my room temperature"

    def test_roast_gpa_lowest(self):
        '''
        Verify roast_gpa() returns the expected message for a gpa higher than or equal to 0.0
        '''
        actual = pyroast.roast_gpa(0.0)
        assert actual == "A gpa that low actually exists? Behold the 8th wonder of the world!"
    
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