# PyRoast

## Build and test status

## Description
pyroast is a lighthearted Python package designed to roast users based on their personal statistics. By taking info like GPA, height, sleep duration, age, and coffee intake, the package evaluates each value to return customized, sarcastic commentary.

## PyPI Package Link

## Installation
1. Install from PyPI with "pip install pyroast"
2. Once installed, import the package into your code with "import pyroast"

## Usage

### Roast_Gpa

#### Evaluates a student's Grade Point Average (GPA) and returns a customized roast.

Parameters: gpa (float | int): The GPA score (e.g., 3.86).

Returns: str — A roast string based on the GPA.

### Roast_Height

#### Generates a roast based on height measured in feet.

Parameters: height (float | int): Height in feet (e.g., 6.0, 5.8).

Returns: str — A roast string evaluating the input height.

### Roast_Sleep

#### Roasts the user based on how many hours of sleep they got last night.

Parameters: hours (float | int): Hours of sleep achieved. Must be a number between 0 and 24 inclusive.

Returns: str — A roast string tailored to the sleep duration.

Raises:

TypeError: If hours is non-numeric or a boolean.

ValueError: If hours is less than 0 or greater than 24.

### Roast_Coffee

#### Evaluates daily caffeine intake and returns a roast based on the number of coffee cups consumed.

Parameters: cups (int | float): Number of cups of coffee drank today.

Returns: str — A roast assessing caffeine dependence.

### Roast_Age

#### Evaluates the user's age in years and returns an age roast.

Parameters: age (int): Age in years. Can be a negative number.

Returns: str — A roast string based on the user's age bracket.

Raises:

TypeError: If age is non-numeric or a boolean.

## Program Examples

### High GPA

print(roast_gpa(3.95))

Output: "I bet you've never known sleep before"

### Tall height

print(roast_height(6.8))

Output: "You might as well just be a tree!"

### 0 hours sleep

print(roast_sleep(0))

Output: "Zero hours? Your eye bags have eye bags."

### A lot of coffee

print(roast_coffee(5))

Output: "Your blood type is officially Espresso."

### Mid 20s

print(roast_age(25))

Output: "Quarter-life crisis mode: fully engaged."

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

## Team members

- [Robert Fang](https://github.com/rfang1224)

- [James Li](https://github.com/DyingRavioli)

- [Danial Sagimbayev](https://github.com/catw1thtea)

- [Pranay Engineer](https://github.com/PranayEng) 

- [Daniyal Malik](https://github.com/DaniyalMlk) 




## Configuration

