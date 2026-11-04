import pytest
from pyroast import pyroast


class TestRoastSleep:

    def test_returns_non_empty_string(self):
        """roast_sleep() returns a non-empty string for a normal value."""
        actual = pyroast.roast_sleep(7)
        assert isinstance(actual, str), f"Expected a string, got {type(actual).__name__}"
        assert len(actual) > 0, "Expected a non-empty roast"

    def test_thresholds_give_different_roasts(self):
        """Each sleep band produces its own roast."""
        bands = [0, 2, 5, 7, 9, 14]
        roasts = [pyroast.roast_sleep(h) for h in bands]
        assert len(set(roasts)) == len(bands), f"Expected {len(bands)} distinct roasts, got {len(set(roasts))}"

    def test_boundaries(self):
        """Values on the edge of a band fall into the expected band."""
        assert pyroast.roast_sleep(0) == "Zero hours? Your eye bags have eye bags."
        assert pyroast.roast_sleep(3.99) == pyroast.roast_sleep(1)
        assert pyroast.roast_sleep(4) == pyroast.roast_sleep(5.5)
        assert pyroast.roast_sleep(8) == pyroast.roast_sleep(10)
        assert pyroast.roast_sleep(10.01) == pyroast.roast_sleep(24)

    def test_accepts_int_and_float(self):
        """Ints and floats in the same band give the same roast."""
        assert pyroast.roast_sleep(7) == pyroast.roast_sleep(7.0)
        assert pyroast.roast_sleep(6) == pyroast.roast_sleep(7.9)

    def test_rejects_out_of_range(self):
        """Negative hours or more than a day raise ValueError."""
        with pytest.raises(ValueError):
            pyroast.roast_sleep(-1)
        with pytest.raises(ValueError):
            pyroast.roast_sleep(24.5)
        with pytest.raises(ValueError):
            pyroast.roast_sleep(100)

    def test_rejects_non_numbers(self):
        """Strings, None and booleans raise TypeError."""
        with pytest.raises(TypeError):
            pyroast.roast_sleep("eight")
        with pytest.raises(TypeError):
            pyroast.roast_sleep(None)
        with pytest.raises(TypeError):
            pyroast.roast_sleep(True)
