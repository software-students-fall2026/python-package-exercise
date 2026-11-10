"""pyroast: a lighthearted package that roasts you based on your stats.

Import the roast functions directly from the package::

    from pyroast import roast_gpa, roast_sleep
    print(roast_sleep(5))

or use the module namespace::

    import pyroast
    print(pyroast.roast_gpa(3.9))
"""

from .pyroast import roast_age, roast_coffee, roast_gpa, roast_height, roast_sleep

__version__ = "0.1.0"

__all__ = [
    "roast_age",
    "roast_coffee",
    "roast_gpa",
    "roast_height",
    "roast_sleep",
    "__version__",
]
