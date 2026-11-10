# PyRoast

## Build and test status

[![build and test](https://github.com/software-students-fall2026/python-package-exercise-team-fast-guys/actions/workflows/build.yml/badge.svg)](https://github.com/software-students-fall2026/python-package-exercise-team-fast-guys/actions/workflows/build.yml)

## Description
pyroast is a lighthearted Python package designed to roast users based on their personal statistics. By taking info like GPA, height, sleep duration, age, and coffee intake, the package evaluates each value to return customized, sarcastic commentary.

## PyPI Package Link

## Installation

Install from PyPI:

```bash
pip install pyroast
```

Then import the functions you want:

```python
from pyroast import roast_gpa, roast_height, roast_sleep, roast_coffee, roast_age
```

or use the package namespace:

```python
import pyroast
print(pyroast.roast_sleep(5))
```

## Usage

### roast_gpa

#### Evaluates a student's Grade Point Average (GPA) and returns a customized roast.

Parameters: gpa (float | int): The GPA score (e.g., 3.86).

Returns: str — A roast string based on the GPA.

### roast_height

#### Generates a roast based on height measured in feet.

Parameters: height (float | int): Height in feet (e.g., 6.0, 5.8).

Returns: str — A roast string evaluating the input height.

### roast_sleep

#### Roasts the user based on how many hours of sleep they got last night.

Parameters: hours (float | int): Hours of sleep achieved. Must be a number between 0 and 24 inclusive.

Returns: str — A roast string tailored to the sleep duration.

Raises:

TypeError: If hours is non-numeric or a boolean.

ValueError: If hours is less than 0 or greater than 24.

### roast_coffee

#### Evaluates daily caffeine intake and returns a roast based on the number of coffee cups consumed.

Parameters: cups (int | float): Number of cups of coffee drank today.

Returns: str — A roast assessing caffeine dependence.

### roast_age

#### Evaluates the user's age in years and returns an age roast.

Parameters: age (int): Age in years. Can be a negative number (counts as "unborn").

Returns: str — A roast string based on the user's age bracket.

Raises:

TypeError: If age is non-numeric or a boolean.

## Program Examples

All examples assume `from pyroast import *` or the explicit import above.

### High GPA

```python
print(roast_gpa(3.95))
# I bet you've never known sleep before
```

### Tall height

```python
print(roast_height(6.8))
# You might as well just be a tree!
```

### 0 hours sleep

```python
print(roast_sleep(0))
# Zero hours? Your eye bags have eye bags.
```

### A lot of coffee

```python
print(roast_coffee(5))
# Your blood has turned into espresso.
```

### Mid 20s

```python
print(roast_age(25))
# Quarter-life crisis mode: fully engaged.
```

### Invalid input

Every function validates its argument and raises a standard Python error you can catch:

```python
try:
    roast_sleep(30)
except ValueError as e:
    print(e)   # hours must be between 0 and 24, got 30

try:
    roast_age("twenty")
except TypeError as e:
    print(e)   # Age should be a whole number of years, instead got str
```

## Example Program

For a complete working example that demonstrates all five package functions in a single script, see:
* 📄 [**Example Script (`__main__.py`)**](./src/pyroast/__main__.py)


## Development setup

### Setting Up Virtual Environment and Dependencies
1. Install `pipenv` if you have not yet using `pip install --user pipenv`.
2. Set up virtual environment using `pipenv shell`.
3. Using `pipenv install`, install project dependencies, including `pytest` for testing.

### Adding and Running Tests
1. Add a new Python file in the `tests` directory for your added method/unit.
    1. Import `pytest` and `pyroast`.
    2. Create a class using `Test` as a prefix and enter methods within it with `test_` as a prefix.
2. Run `pytest` to run tests in the `tests` directory.

Pull requests will build and test with Github Actions.

## Team members

- [Robert Fang](https://github.com/rfang1224)

- [James Li](https://github.com/DyingRavioli)

- [Danial Sagimbayev](https://github.com/catw1thtea)

- [Pranay Engineer](https://github.com/PranayEng) 

- [Daniyal Malik](https://github.com/DaniyalMlk) 

