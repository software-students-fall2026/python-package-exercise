"""
In Python packages, this file called __main__.py is run when the package is run
directly from command line, as opposed to importing it into another program.
"""

from pyroast import pyroast


def main():
    print("Welcome to Pyroast")
    
    print("GPA Roast (3.86):", pyroast.roast_gpa(3.86))
    print("Height Roast (5.0):", pyroast.roast_height(5.0))


if __name__ == "__main__":
    main()