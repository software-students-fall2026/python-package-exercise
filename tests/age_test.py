import pytest
from pyroast import pyroast

class TestAgeRoast:
    def test_roast_age_different(self):
        """
        Verify roast_age returns a string for different age inputs.
        """
        sample_ages = [-23, 1, 10, 20, 30, 40, 65, 90, 129000]
        sample_results = set(pyroast.roast_age(a) for a in sample_ages)
        assert len(sample_ages) == len(sample_results), f"Expected {len(sample_ages)} responses. Got {len(sample_results)} responses instead."

    def test_roast_age_non_ints(self):
        """
        Verify roast_age raises a Type Error if a non-integer value is passed.
        """
        with pytest.raises(TypeError):
            pyroast.roast_age(2.332)
        with pytest.raises(TypeError):
            pyroast.roast_age("32")
        with pytest.raises(TypeError):
            pyroast.roast_age(True)
        with pytest.raises(TypeError):
            pyroast.roast_age([42])

    def test_roast_age_return_str(self):
        """
        Verify roast_age returns a string if passed a int.
        """
        result = pyroast.roast_age(32)
        assert isinstance(result, str), f"Expected roast_age() to return a string. Instead got {type(result).__name__}"