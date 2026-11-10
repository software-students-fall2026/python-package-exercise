import pyroast


class TestPackageExports:

    def test_functions_importable_from_package(self):
        """All five roast functions are exposed at the package top level."""
        for name in ("roast_gpa", "roast_height", "roast_coffee", "roast_sleep", "roast_age"):
            assert hasattr(pyroast, name), f"pyroast.{name} is not exported"
            assert callable(getattr(pyroast, name)), f"pyroast.{name} is not callable"

    def test_from_import_matches_module_function(self):
        """`from pyroast import roast_gpa` is the same object as pyroast.pyroast.roast_gpa."""
        from pyroast import roast_gpa
        from pyroast.pyroast import roast_gpa as module_roast_gpa
        assert roast_gpa is module_roast_gpa

    def test_all_lists_every_export(self):
        """__all__ names each public function and the version."""
        assert set(pyroast.__all__) >= {"roast_gpa", "roast_height", "roast_coffee", "roast_sleep", "roast_age"}
        assert "__version__" in pyroast.__all__

    def test_version_is_a_string(self):
        """__version__ exists and looks like a semantic version."""
        assert isinstance(pyroast.__version__, str)
        parts = pyroast.__version__.split(".")
        assert len(parts) == 3, f"Expected MAJOR.MINOR.PATCH, got {pyroast.__version__}"
        assert all(p.isdigit() for p in parts)

    def test_top_level_call_works(self):
        """Calling through the package namespace returns a roast."""
        result = pyroast.roast_sleep(7)
        assert isinstance(result, str) and result
