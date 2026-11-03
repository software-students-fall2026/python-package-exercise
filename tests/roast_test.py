import pytest
from pyroast import pyroast

class Test:

    def test_roast_gpa(self):
        '''
        Verify roast_gpa() returns a non-empty string.
        '''
        actual = pyroast.roast_gpa(3.86)
        assert isinstance(actual, str), f"Expected roast_gpa() to return a string. Instead, it returned {actual}"
        assert len(actual) > 0, f"Expected roast_gpa() not to be empty. Instead, it returned a string with {len(actual)} characters"